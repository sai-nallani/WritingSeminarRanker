import json

with open("./data.txt") as f:
    data = f.read().splitlines()

Courses = {}
i = 0
while i < len(data):
    line = data[i].strip()
    # Find course title: line not empty, next line starts with WRI, next next line not blank
    if line and i + 1 < len(data) and data[i + 1].strip().startswith("WRI") and (i + 2 < len(data) and data[i + 2].strip()):
        course_title = line
        i += 1
        # Gather all course timings (lines starting with WRI)
        course_timings = []
        while i < len(data) and data[i].strip().startswith("WRI"):
            course_timings.append(data[i].strip())
            i += 1
        # Next non-empty line is instructor
        while i < len(data) and not data[i].strip():
            i += 1
        course_instructor = data[i].strip() if i < len(data) else ""
        i += 1
        # Gather all lines until next course or end, and find the longest line for description
        desc_lines = []
        while i < len(data):
            # Look ahead for next course title
            if data[i].strip() and (i + 1 < len(data) and data[i + 1].strip().startswith("WRI") and (i + 2 < len(data) and data[i + 2].strip())):
                break
            if data[i].strip():
                desc_lines.append(data[i].strip())
            i += 1
        # The longest line is the description
        course_description = max(desc_lines, key=len) if desc_lines else ""
        Courses[course_title] = {
            "course_timings": course_timings,
            "course_instructor": course_instructor,
            "course_description": course_description
        }
    else:
        i += 1

# Write to JSON file
with open("courses.json", "w") as f:
    json.dump(Courses, f, indent=2)
