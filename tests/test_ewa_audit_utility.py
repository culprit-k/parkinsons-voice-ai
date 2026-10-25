import json
import subprocess
import sys
import tempfile
import unittest
import wave
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "audit_ewa_db_local.py"


def make_wav(path: Path, rate: int, frames: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "wb") as out:
        out.setnchannels(1)
        out.setsampwidth(2)
        out.setframerate(rate)
        out.writeframes(b"\x00\x00" * frames)


class EwaAuditUtilityTests(unittest.TestCase):
    def test_aggregate_output_is_private_and_counts_are_correct(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            pd_audio = base / "PD" / "p-private-001" / "phonation" / "recording-private-a.wav"
            hc_audio = base / "HC" / "c-private-001" / "phonation" / "recording-private-b.wav"
            other_audio = base / "HC" / "c-private-002" / "pataka" / "recording-private-c.wav"
            make_wav(pd_audio, 16000, 16000)
            # Identical content across labels intentionally tests cross-group duplicate detection.
            make_wav(hc_audio, 16000, 16000)
            make_wav(other_audio, 8000, 4000)
            report_path = base / "safe-output.json"
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--root", str(base), "--pd-dir", "PD",
                 "--control-dir", "HC", "--task-dir", "phonation", "--out", str(report_path)],
                check=False, capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, msg=result.stderr + result.stdout)
            data = json.loads(report_path.read_text(encoding="utf-8"))
            self.assertEqual(data["cohort_summary"]["pd_participant_folders_with_wav"], 1)
            self.assertEqual(data["cohort_summary"]["control_participant_folders_with_wav"], 2)
            self.assertEqual(data["group_audio_summary"]["PD"]["readable_pcm_wav_headers"], 1)
            self.assertEqual(data["group_audio_summary"]["healthy_control"]["readable_pcm_wav_headers"], 2)
            self.assertEqual(data["cross_group_exact_duplicate_audio_hash_groups"], 1)
            self.assertTrue(data["privacy"]["aggregate_counts_only"])
            serialized = json.dumps(data)
            for private_fragment in (
                "p-private-001", "c-private-001", "c-private-002",
                "recording-private-a.wav", "recording-private-b.wav",
                "recording-private-c.wav", str(base),
            ):
                self.assertNotIn(private_fragment, serialized)

    def test_missing_class_folder_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            (base / "PD").mkdir()
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--root", str(base), "--pd-dir", "PD",
                 "--control-dir", "HC", "--out", str(base / "out.json")],
                check=False, capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 2)
            self.assertFalse((base / "out.json").exists())


if __name__ == "__main__":
    unittest.main()
