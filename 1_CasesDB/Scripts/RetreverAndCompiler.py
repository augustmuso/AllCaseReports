# python class that locates either group or one case from a AllCase.db, collects patient information including pics and graphs if any  and complies it or each to form a specific latex section that is to be used and part of case report and case report presenattion 


import sqlite3
from jinja2 import Template

class CaseReportCompiler:
    def __init__(self, db_path):
        self.db_path = db_path

    def fetch_case_data(self, case_id=None, group_id=None):
        """
        Fetch case data based on either a single case ID or a group ID.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        if case_id:
            cursor.execute("SELECT * FROM cases WHERE id=?", (case_id,))
        elif group_id:
            cursor.execute("SELECT * FROM cases WHERE group_id=?", (group_id,))
        else:
            raise ValueError("Specify either case_id or group_id")

        cases = cursor.fetchall()
        conn.close()

        case_data = []
        for case in cases:
            case_data.append(self.structure_case_data(case))
        return case_data

    def structure_case_data(self, case):
        """
        Organize case information into a dictionary format.
        """
        case_id, patient_name, age, gender, diagnosis, treatment, image_path, graph_path = case
        return {
            "id": case_id,
            "name": patient_name,
            "age": age,
            "gender": gender,
            "diagnosis": diagnosis,
            "treatment": treatment,
            "image": image_path,
            "graph": graph_path
        }

    def generate_latex_section(self, case_data):
        """
        Create a LaTeX section for each case.
        """
        latex_template = """
        \\section*{Case {{ case.id }}: {{ case.name }}}
        \\textbf{Age:} {{ case.age }} \\
        \\textbf{Gender:} {{ case.gender }} \\
        \\textbf{Diagnosis:} {{ case.diagnosis }} \\
        \\textbf{Treatment:} {{ case.treatment }} \\

        {% if case.image %}
        \\begin{figure}[h]
            \\centering
            \\includegraphics[width=0.5\\textwidth]{ {{ case.image }} }
            \\caption{Patient image}
        \\end{figure}
        {% endif %}

        {% if case.graph %}
        \\begin{figure}[h]
            \\centering
            \\includegraphics[width=0.5\\textwidth]{ {{ case.graph }} }
            \\caption{Diagnostic graph}
        \\end{figure}
        {% endif %}
        """
        template = Template(latex_template)
        latex_sections = [template.render(case=case) for case in case_data]
        return "\n".join(latex_sections)

    def compile_report(self, case_id=None, group_id=None):
        """
        Fetch, structure, and compile case data into LaTeX format.
        """
        case_data = self.fetch_case_data(case_id, group_id)
        return self.generate_latex_section(case_data)
