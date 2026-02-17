import json
import zipfile
from pathlib import Path
from datetime import datetime
import platform

from dicegame.logging.config import LOG_DIR
from dicegame.logging.config import redact
from dicegame.session.session_disk import Session


APP_NAME = "dicegame"


def _collect_metadata() -> dict:
    return {
        "app": APP_NAME,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "os": platform.system(),
        "os_version": platform.version(),
        "python_version": platform.python_version(),
    }


def _collect_logs() -> list[Path]:
    if not LOG_DIR.exists():
        return []
    return sorted(LOG_DIR.glob("*.log"))


def report_bug_service(session: Session) -> Path | None:
    logs = _collect_logs()
    metadata = _collect_metadata()

    if not logs:
        print("No logs found to report.")
        return None

    print("\nBug report will include:")
    print("- Application metadata (version, OS, Python)")
    print("- Log files:")
    for log in logs:
        print(f"  • {log.name}")

    print("\n⚠️  No passwords, tokens, or secrets are included.")

    #if interactive is True:
    confirm = input("\nCreate bug report archive? [y/N]: ").strip().lower()
    if confirm != "y":
        return None

    report_dir = Path.home() / ".local/share" / APP_NAME / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)

    archive_path = report_dir / f"bug-report-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}.zip"

    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(
            "metadata.json",
            json.dumps(redact(metadata), indent=2),
        )

        for log in logs:
            zf.write(log, arcname=f"logs/{log.name}")

    return archive_path
