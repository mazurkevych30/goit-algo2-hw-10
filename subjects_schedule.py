# Визначення класу Teacher
class Teacher:

    def __init__(
        self,
        first_name: str,
        last_name: str,
        age: int,
        email: str,
        can_teach_subjects: set[str],
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()


def create_schedule(
    subjects: set[str], teachers: list[Teacher]
) -> list[Teacher] | None:
    sorted_teachers = sorted(teachers, key=lambda t: t.age)

    chosen_teachers: list[Teacher] = []
    uncovered_subjects = subjects.copy()

    while uncovered_subjects:
        available_teachers = [
            teacher
            for teacher in sorted_teachers
            if teacher not in chosen_teachers
            and len(teacher.can_teach_subjects & uncovered_subjects) > 0
        ]

        if not available_teachers:
            return None

        best_teacher = max(
            available_teachers,
            key=lambda teacher: len(teacher.can_teach_subjects & uncovered_subjects),
        )

        covered_subjects = best_teacher.can_teach_subjects & uncovered_subjects
        best_teacher.assigned_subjects.update(covered_subjects)
        chosen_teachers.append(best_teacher)

        uncovered_subjects -= covered_subjects

    if uncovered_subjects:
        return None

    return chosen_teachers


if __name__ == "__main__":
    # Множина предметів
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія", "Невідомий"}
    # Створення списку викладачів
    teachers = [
        Teacher(
            first_name="Олександр",
            last_name="Іваненко",
            age=45,
            email="o.ivanenko@example.com",
            can_teach_subjects={"Математика", "Фізика"},
        ),
        Teacher(
            first_name="Марія",
            last_name="Петренко",
            age=38,
            email="m.petrenko@example.com",
            can_teach_subjects={"Хімія"},
        ),
        Teacher(
            first_name="Сергій",
            last_name="Коваленко",
            age=50,
            email="s.kovalenko@example.com",
            can_teach_subjects={"Інформатика", "Математика"},
        ),
        Teacher(
            first_name="Наталія",
            last_name="Шевченко",
            age=29,
            email="n.shevchenko@example.com",
            can_teach_subjects={"Біологія", "Хімія"},
        ),
        Teacher(
            first_name="Дмитро",
            last_name="Бондаренко",
            age=35,
            email="d.bondarenko@example.com",
            can_teach_subjects={"Фізика", "Інформатика"},
        ),
        Teacher(
            first_name="Олена",
            last_name="Гриценко",
            age=42,
            email="o.grytsenko@example.com",
            can_teach_subjects={"Біологія"},
        ),
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}"
            )
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
