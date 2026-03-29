# File Organizer Script

A Python utility that scans a target directory and sorts files into categorized subfolders automatically.

## 🔧 Features

- Recursively scans the target folder
- Sorts files into categories by extension
- Creates category folders automatically
- Supports common categories:
  - `Images` (jpg, jpeg, png, gif, bmp, tiff, webp, etc.)
  - `Videos` (mp4, mkv, avi, mov, webm, etc.)
  - `Documents` (pdf, docx, txt, xlsx, pptx, etc.)
  - `Audio` (mp3, wav, flac, m4a, aac, etc.)
  - `Archives` (zip, rar, tar, gz, 7z, etc.)
  - `Scripts` (py, js, sh, bat, etc.)
  - `Others` (unrecognized extensions)

## ▶️ Usage

1. Ensure Python is installed:

```bash
python3 --version
```

2. Run the script:

```bash
python file_organizer_script.py /path/to/target-directory
```

3. Optional CLI flags (if implemented):

```bash
python file_organizer_script.py /path/to/target-directory --dry-run
python file_organizer_script.py /path/to/target-directory --verbose
```

## 🛠️ Example

Before:
- downloads/todo.txt
- downloads/movie.mp4
- downloads/photo.jpg
- downloads/notes.docx

After:
- downloads/Documents/todo.txt
- downloads/Videos/movie.mp4
- downloads/Images/photo.jpg
- downloads/Documents/notes.docx

## 💡 Implementation notes

- Use `argparse` for CLI options
- Validate target folder exists and is readable
- Use `os.walk` to traverse files
- Use `shutil.move` to relocate files
- Ensure category folders are skipped during traversal (avoid re-processing)
- Handle duplicate names (e.g., append counter)

## 📚 Skills learned

- File system operations (os, shutil)
- Automation scripts
- Path management and error handling
- CLI and user options

## License

This project is open source and available under the [MIT License](LICENSE).