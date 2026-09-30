#!/usr/bin/env python3
"""
Parse fullstack_developer_syllabus.txt and draw the full folder structure
inside syllabus_explanation/, one folder per MODULE > SECTION > LESSON.

Rules:
- Existing module-level README.md files are NEVER touched.
- Every section folder and lesson folder gets an empty README.md placeholder
  (created only if absent; never overwritten).
- Numbering gaps from the syllabus are preserved exactly.
- Writes syllabus_explanation/STRUCTURE.md with the full tree (including
  PRACTICE items, which do not get their own folders).
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYLLABUS = os.path.join(ROOT, "fullstack_developer_syllabus.txt")
OUT = os.path.join(ROOT, "syllabus_explanation")

MODULE_DIRS = {
    "01": "01-introduction",
    "02": "02-html-and-css-fundamentals",
    "03": "03-javascript-fundamentals",
    "04": "04-tools-of-the-trade",
    "05": "05-accessible-development",
    "06": "06-essential-css",
    "07": "07-essential-javascript",
    "08": "08-responsive-design",
    "09": "09-apis-and-async-javascript",
    "10": "10-ai-engineering",
    "11": "11-node-js",
    "12": "12-databases",
    "13": "13-express-js",
    "14": "14-user-interface-design",
    "15": "15-react-js-fundamentals",
    "16": "16-testing",
    "17": "17-advanced-react-js",
    "18": "18-typescript",
    "19": "19-next-js",
    "20": "20-launching-your-career",
}


def slugify(title: str) -> str:
    t = title.strip().replace("_", "")
    t = re.sub(r"[^A-Za-z0-9\s]", " ", t)
    t = re.sub(r"\s+", "-", t.strip())
    t = re.sub(r"-{2,}", "-", t).strip("-").lower()
    return t or "untitled"


def parse_syllabus(path: str):
    modules = []
    current_module = None
    current_section = None
    current_lesson = None
    focus_pending = None

    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")

            m = re.match(r"^MODULE (\d{2})\.\s+(.+?)\s*$", line)
            if m:
                current_module = {
                    "num": m.group(1),
                    "title": m.group(2),
                    "focus": "",
                    "sections": [],
                }
                modules.append(current_module)
                current_section = None
                current_lesson = None
                focus_pending = current_module
                continue

            if focus_pending is not None and line.startswith("Learning focus:"):
                focus_pending["focus"] = line.split(":", 1)[1].strip()
                focus_pending = None
                continue

            m = re.match(r"^\s+SECTION / UNIT: (\d{2})\.\s+(.+?)\s*$", line)
            if m and current_module is not None:
                current_section = {
                    "num": m.group(1),
                    "title": m.group(2),
                    "lessons": [],
                }
                current_module["sections"].append(current_section)
                current_lesson = None
                continue

            m = re.match(r"^\s+LESSON / ACTIVITY: (?:(\d{2})\.\s+)?(.+?)\s*$", line)
            if m and current_section is not None:
                current_lesson = {
                    "num": m.group(1) or "",
                    "title": m.group(2),
                    "practices": [],
                }
                current_section["lessons"].append(current_lesson)
                continue

            m = re.match(r"^\s+PRACTICE: (.+?)\s*$", line)
            if m:
                if current_lesson is not None:
                    current_lesson["practices"].append(m.group(1))
                continue

            focus_pending = None

    return modules


def main():
    modules = parse_syllabus(SYLLABUS)

    n_sections = n_lessons = n_practices = 0
    n_dirs_created = n_readmes_created = 0
    skipped_existing_readmes = []

    tree_lines = [
        "# Full Syllabus Structure (drawn from fullstack_developer_syllabus.txt)",
        "",
        "Folder map of every module, section and lesson. Each section/lesson folder",
        "contains an empty `README.md` placeholder to be filled lesson-by-lesson in",
        "Hinglish from the course transcript. PRACTICE items are documented inside",
        "their parent lesson README (they do not get separate folders).",
        "",
        "Module-level `README.md` files already present are untouched.",
        "",
        "```",
    ]

    for mod in modules:
        mod_dir = MODULE_DIRS.get(mod["num"])
        if mod_dir is None:
            sys.exit(f"No folder mapping for module {mod['num']}")
        mod_path = os.path.join(OUT, mod_dir)
        os.makedirs(mod_path, exist_ok=True)

        tree_lines.append(f"{mod_dir}/  <- MODULE {mod['num']}. {mod['title']}")
        if os.path.exists(os.path.join(mod_path, "README.md")):
            tree_lines.append(f"    README.md  (module overview - exists, untouched)")

        for sec in mod["sections"]:
            n_sections += 1
            sec_slug = f"{sec['num']}-{slugify(sec['title'])}"
            sec_path = os.path.join(mod_path, sec_slug)
            if not os.path.isdir(sec_path):
                n_dirs_created += 1
            os.makedirs(sec_path, exist_ok=True)

            sec_readme = os.path.join(sec_path, "README.md")
            if not os.path.exists(sec_readme):
                open(sec_readme, "w").close()
                n_readmes_created += 1

            tree_lines.append(f"    {sec_slug}/  <- SECTION {sec['num']}. {sec['title']}")

            if not sec["lessons"]:
                tree_lines.append(f"        README.md  (section notes")

            for les in sec["lessons"]:
                n_lessons += 1
                les_slug = f"{les['num']}-{slugify(les['title'])}" if les["num"] else slugify(les["title"])
                les_path = os.path.join(sec_path, les_slug)
                if not os.path.isdir(les_path):
                    n_dirs_created += 1
                os.makedirs(les_path, exist_ok=True)

                les_readme = os.path.join(les_path, "README.md")
                if not os.path.exists(les_readme):
                    open(les_readme, "w").close()
                    n_readmes_created += 1
                else:
                    skipped_existing_readmes.append(les_readme)

                label = f"LESSON {les['num']}. {les['title']}" if les["num"] else f"LESSON: {les['title']}"
                tree_lines.append(f"        {les_slug}/  <- {label}")
                for prac in les["practices"]:
                    n_practices += 1
                    tree_lines.append(f"            - PRACTICE: {prac}")

    tree_lines.append("```")
    tree_lines.append("")
    tree_lines.append("## Totals")
    tree_lines.append("")
    tree_lines.append(f"- Modules: {len(modules)}")
    tree_lines.append(f"- Sections: {n_sections}")
    tree_lines.append(f"- Lessons / activities: {n_lessons}")
    tree_lines.append(f"- Practice items (listed in lesson READMEs): {n_practices}")
    tree_lines.append("")
    tree_lines.append("## Module map")
    tree_lines.append("")
    for mod in modules:
        tree_lines.append(f"- MODULE {mod['num']}. {mod['title']} — {mod['focus']}")
    tree_lines.append("")

    struct_path = os.path.join(OUT, "STRUCTURE.md")
    with open(struct_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(tree_lines))

    print(f"modules parsed        : {len(modules)}")
    print(f"sections              : {n_sections}")
    print(f"lessons               : {n_lessons}")
    print(f"practices             : {n_practices}")
    print(f"dirs created          : {n_dirs_created}")
    print(f"empty READMEs created : {n_readmes_created}")
    print(f"existing READMEs kept : {len(skipped_existing_readmes)}")
    print(f"structure file        : {struct_path}")


if __name__ == "__main__":
    main()
