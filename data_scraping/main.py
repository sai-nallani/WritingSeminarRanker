import json

with open("./data.txt", encoding="utf-8") as f:
    data = f.read().splitlines()

Courses = {}
i = 0
while i < len(data):
    line = data[i].strip()

    # More flexible: a course title is followed by a WRI line
    if line and i + 1 < len(data) and data[i + 1].strip().startswith("WRI"):
        course_title = line
        i += 1

        # Gather course timings
        course_timings = []
        while i < len(data) and data[i].strip().startswith("WRI"):
            course_timings.append(data[i].strip())
            i += 1

        # Skip empty lines to find instructor
        while i < len(data) and not data[i].strip():
            i += 1
        course_instructor = data[i].strip() if i < len(data) else ""
        i += 1

        # Collect description until next course title or end of file
        desc_lines = []
        while i < len(data):
            # Look ahead for next course start
            next_line = data[i].strip()
            next_next_line = data[i+1].strip() if i + 1 < len(data) else ""
            if next_line and next_next_line.startswith("WRI"):
                break
            if next_line:
                desc_lines.append(next_line)
            i += 1

        course_description = " ".join(desc_lines)

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
