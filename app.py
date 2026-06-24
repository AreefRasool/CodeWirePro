!pip install gradio reportlab

import gradio as gr
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

projects = {}

def voltage_drop(voltage, current, length, resistance):
    if voltage <= 0:
        return "❌ Invalid Voltage"
    drop = (2 * current * length * resistance) / 1000
    percent = (drop / voltage) * 100
    status = "✅ COMPLIANT" if percent <= 3 else "⚠ ACCEPTABLE" if percent <= 5 else "❌ NON-COMPLIANT"
    return f"""# ⚡ Voltage Drop Analysis

- Voltage Drop: **{drop:.2f} V**
- Loss Percentage: **{percent:.2f}%**
- Status: **{status}**
"""

def wire_size(current):
    if current <= 10: wire = "14 AWG (1.5 mm²)"
    elif current <= 16: wire = "12 AWG (2.5 mm²)"
    elif current <= 25: wire = "10 AWG (4 mm²)"
    elif current <= 35: wire = "8 AWG (6 mm²)"
    else: wire = "6 AWG (10 mm²)"
    return f"# 🔌 Wire Sizing Report\n\n**Recommended Wire:** {wire}\n\n**Load Current:** {current} A"

def conduit_fill(wires):
    fill = wires * 12
    if fill <= 40:
        conduit, status = "1/2 inch", "SAFE"
    elif fill <= 60:
        conduit, status = "3/4 inch", "NORMAL"
    elif fill <= 80:
        conduit, status = "1 inch", "HIGH"
    else:
        conduit, status = "1.25 inch+", "OVERLOADED"
    return f"# 📦 Conduit Fill Report\n\n- Fill: **{fill}%**\n- Conduit: **{conduit}**\n- Status: **{status}**"

def box_fill(conductors, devices, grounds):
    volume = (conductors * 2) + (devices * 2) + grounds
    return f"# 📐 Box Fill Report\n\n**Required Volume:** {volume}"

def ampacity(size):
    table = {"14 AWG":15,"12 AWG":20,"10 AWG":30,"8 AWG":40,"6 AWG":55}
    return f"# 🔥 Ampacity Report\n\n**Safe Current Capacity:** {table.get(size,'Unknown')} A"

def estimate_material(length):
    return f"""# 📋 Material Estimation

- Wire Required: **{length*1.10:.2f} m**
- Conduit Required: **{length:.2f} m**
"""

def generate_report(project_name, voltage, current, length, resistance,
                    current_wire, wires, conductors, devices, grounds,
                    size, material_length):

    vd = voltage_drop(voltage,current,length,resistance)
    ws = wire_size(current_wire)
    cf = conduit_fill(wires)
    bf = box_fill(conductors,devices,grounds)
    ap = ampacity(size)
    mt = estimate_material(material_length)

    return f"""
# ⚡ CODEWIRE ENGINEERING REPORT

## 📂 Project Name
**{project_name or 'Unnamed Project'}**

---

{vd}

---

{ws}

---

{cf}

---

{bf}

---

{ap}

---

{mt}

---

## ✅ Summary
All modules analyzed successfully.
"""

def save_project(name, report):
    if not name:
        return "❌ Enter Project Name"
    projects[name] = report
    return f"✅ Project '{name}' Saved"

def export_pdf(project_name, report_text):
    filename = f"{project_name or 'Codewire_Report'}.pdf"
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = [
        Paragraph("CODEWIRE ENGINEERING REPORT", styles["Title"]),
        Spacer(1, 12),
        Paragraph(report_text.replace("\n", "<br/>"), styles["BodyText"])
    ]

    doc.build(content)
    return filename

css = """
.gradio-container{max-width:1400px!important}
.main-title{text-align:center;padding:25px;border-radius:20px;background:linear-gradient(135deg,#1e293b,#0f172a);}
.card{text-align:center;padding:15px;border-radius:15px;background:#1e293b;border:1px solid #334155;}
"""

with gr.Blocks(css=css, theme=gr.themes.Base()) as app:

    gr.HTML("""
    <div class="main-title">
    <h1>⚡ CODEWIRE</h1>
    <h3>Electrical Code Compliance Platform</h3>
    <p>Voltage Drop • Wire Sizing • Conduit Fill • Box Fill • Ampacity • Material Estimation</p>
    </div>
    """)

    with gr.Row():
        gr.HTML('<div class="card"><h2>⚡ 6 Modules</h2></div>')
        gr.HTML('<div class="card"><h2>🟢 System Online</h2></div>')
        gr.HTML('<div class="card"><h2>📂 Project Manager</h2></div>')

    project_name = gr.Textbox(label="Project Name")

    with gr.Tabs():
        with gr.Tab("⚡ Voltage Drop"):
            voltage = gr.Number(label="Voltage", value=230)
            current = gr.Number(label="Current", value=10)
            length = gr.Number(label="Length", value=50)
            resistance = gr.Number(label="Resistance", value=0.5)
            out1 = gr.Markdown()
            gr.Button("Run Analysis").click(voltage_drop,[voltage,current,length,resistance],out1)

        with gr.Tab("🔌 Wire Sizing"):
            current2 = gr.Number(label="Current", value=18)
            out2 = gr.Markdown()
            gr.Button("Recommend Wire").click(wire_size,current2,out2)

        with gr.Tab("📦 Conduit Fill"):
            wires = gr.Number(label="Wire Count", value=5)
            out3 = gr.Markdown()
            gr.Button("Analyze Conduit").click(conduit_fill,wires,out3)

        with gr.Tab("📐 Box Fill"):
            conductors = gr.Number(label="Conductors", value=8)
            devices = gr.Number(label="Devices", value=2)
            grounds = gr.Number(label="Grounds", value=1)
            out4 = gr.Markdown()
            gr.Button("Calculate Box Fill").click(box_fill,[conductors,devices,grounds],out4)

        with gr.Tab("🔥 Ampacity"):
            size = gr.Dropdown(["14 AWG","12 AWG","10 AWG","8 AWG","6 AWG"], value="12 AWG", label="Wire Size")
            out5 = gr.Markdown()
            gr.Button("Check Ampacity").click(ampacity,size,out5)

        with gr.Tab("📋 Material Estimator"):
            est_len = gr.Number(label="Cable Length (m)", value=50)
            est_out = gr.Markdown()
            gr.Button("Estimate Materials").click(estimate_material,est_len,est_out)

        with gr.Tab("📄 Reports"):
            report_out = gr.Markdown()

            gr.Button("Generate Complete Engineering Report").click(
                generate_report,
                [project_name, voltage, current, length, resistance,
                 current2, wires, conductors, devices, grounds,
                 size, est_len],
                report_out
            )

            save_status = gr.Markdown()

            gr.Button("💾 Save Project").click(
                save_project,
                [project_name, report_out],
                save_status
            )

            pdf_file = gr.File(label="📄 Download PDF")

            gr.Button("📄 Export PDF").click(
                export_pdf,
                [project_name, report_out],
                pdf_file
            )

app.launch(share=True)
