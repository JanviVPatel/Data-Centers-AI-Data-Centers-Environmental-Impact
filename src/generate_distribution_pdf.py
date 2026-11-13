import os
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

PDF_PATH = Path("C:/Users/janvi/Desktop/EDA Project/report/EDA_Project_Progress_and_Work_Distribution.pdf")
PDF_PATH.parent.mkdir(parents=True, exist_ok=True)

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#555555"))
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 750, "IT 462: Exploratory Data Analysis | Environmental Impact of Data Centers")
            self.setStrokeColor(colors.HexColor("#D0D7DE"))
            self.setLineWidth(0.5)
            self.line(54, 742, 558, 742)
        # Footer
        self.setStrokeColor(colors.HexColor("#D0D7DE"))
        self.setLineWidth(0.5)
        self.line(54, 45, 558, 45)
        self.drawString(54, 32, "DA-IICT | Dr. Gopinath Panda | Project Blueprint & Work Plan")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 32, page_str)
        self.restoreState()

def build_pdf():
    doc = SimpleDocTemplate(
        str(PDF_PATH),
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#0B2545'),
        alignment=0,
        spaceAfter=4
    )
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#134074'),
        spaceAfter=15
    )
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#0B2545'),
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )
    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#134074'),
        spaceBefore=10,
        spaceAfter=5,
        keepWithNext=True
    )
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#1D2D44'),
        spaceAfter=6
    )
    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#1D2D44'),
        leftIndent=15,
        spaceAfter=3
    )
    callout_style = ParagraphStyle(
        'Callout',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#0B2545')
    )
    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#1D2D44')
    )
    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#0B2545')
    )

    story = []

    # Title & Metadata
    story.append(Paragraph("Project Status Report & 4-Member Work Distribution", title_style))
    story.append(Paragraph("<b>Course:</b> IT 462 — Exploratory Data Analysis | <b>Mentor:</b> Dr. Gopinath Panda | <b>DA-IICT</b>", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#134074'), spaceAfter=12))

    # Meta banner table
    meta_data = [
        [
            Paragraph("<b>Project Title:</b> Environmental Impact of Data Centers & AI Data Centers", table_cell),
            Paragraph("<b>Repository:</b> JanviVPatel/Data-Centers-AI-Data-Centers-Environmental-Impact", table_cell)
        ],
        [
            Paragraph("<b>Target Format:</b> DA-IICT IT462_2026 Academic Report", table_cell),
            Paragraph("<b>Status:</b> Phase 1 Completed (Data Acquired & Verified)", table_cell)
        ]
    ]
    t_meta = Table(meta_data, colWidths=[270, 234])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#EEF4F8')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#8DA9C4')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#D0D7DE')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 14))

    # SECTION 1: What We Have Done So Far
    story.append(Paragraph("1. Summary of Completed Work (Phase 1)", h1_style))
    story.append(Paragraph(
        "Phase 1 has established the foundations for the project in accordance with the IT 462 syllabus and Dr. Panda's requirements:",
        body_style
    ))
    
    story.append(Paragraph("• <b>Workspace & Directory Architecture:</b> Configured a clean project folder on the local machine at <code>C:\\Users\\janvi\\Desktop\\EDA Project\\</code> with isolated subdirectories: <code>data/processed/</code>, <code>notebooks/</code>, <code>src/</code>, <code>report/figures/</code>, and <code>reference/</code>.", bullet_style))
    story.append(Paragraph("• <b>Reference Benchmark Analysis:</b> Analyzed the senior reference project (<code>Group23_RoadAccidents.ipynb</code> & report) to map the exact required diagnostic plots, ML models, and chapter sections.", bullet_style))
    story.append(Paragraph("• <b>Environment & Dependency Setup:</b> Installed and verified all core libraries, including <code>missingno</code> (missing data matrices, dendrograms), <code>folium</code> (geospatial mapping), <code>scikit-learn</code>, <code>seaborn</code>, <code>scipy</code>, and <code>reportlab</code>.", bullet_style))
    story.append(Paragraph("• <b>Automated Dataset Acquisition:</b> Downloaded, verified, and extracted <b>10 out of 13 datasets (~6.88 GB, 67,091 files)</b> into dedicated subfolders under <code>EDA Data/</code>.", bullet_style))
    story.append(Paragraph("• <b>Documentation & Audit:</b> Preserved original README and scripts, generated <code>dataset_download_status.md</code>, and created a root <code>.gitignore</code> to protect the GitHub repository from multi-gigabyte data files.", bullet_style))

    story.append(Spacer(1, 8))

    # Datasets Table
    d_rows = [
        [Paragraph("ID", table_cell_bold), Paragraph("Dataset Name", table_cell_bold), Paragraph("Source", table_cell_bold), Paragraph("Status", table_cell_bold), Paragraph("Files / Volume", table_cell_bold)],
        [Paragraph("D1", table_cell), Paragraph("AI Data Centers", table_cell), Paragraph("Epoch AI", table_cell), Paragraph("✅ Verified", table_cell), Paragraph("1 CSV (72 KB)", table_cell)],
        [Paragraph("D2", table_cell), Paragraph("GenAI Workload Power Profiles", table_cell), Paragraph("DOE / NLR", table_cell), Paragraph("✅ Verified", table_cell), Paragraph("3,148 CSV traces (3.78 GB)", table_cell)],
        [Paragraph("D3", table_cell), Paragraph("IM3 Data Center Atlas", table_cell), Paragraph("PNNL / OSTI", table_cell), Paragraph("✅ Verified", table_cell), Paragraph("1 GeoPackage (824 KB)", table_cell)],
        [Paragraph("D4", table_cell), Paragraph("Open U.S. Data Centers Tracker", table_cell), Paragraph("FracTracker", table_cell), Paragraph("✅ Verified", table_cell), Paragraph("1,733 facilities (3.83 MB)", table_cell)],
        [Paragraph("D5", table_cell), Paragraph("IM3 Projected Locations 2035", table_cell), Paragraph("DOE / PNNL", table_cell), Paragraph("✅ Verified", table_cell), Paragraph("Projections repo (250 MB)", table_cell)],
        [Paragraph("D6", table_cell), Paragraph("Data Center Load Projections", table_cell), Paragraph("EPRI", table_cell), Paragraph("⚠️ Manual", table_cell), Paragraph("Interactive dashboard portal", table_cell)],
        [Paragraph("D7", table_cell), Paragraph("EIA-930 Hourly Grid Monitor", table_cell), Paragraph("U.S. EIA", table_cell), Paragraph("✅ Verified", table_cell), Paragraph("44-col balance CSV (39.8 MB)", table_cell)],
        [Paragraph("D8", table_cell), Paragraph("eGRID Emissions & Fuel Mix", table_cell), Paragraph("U.S. EPA", table_cell), Paragraph("✅ Verified", table_cell), Paragraph("1 Excel workbook (20.2 MB)", table_cell)],
        [Paragraph("D9", table_cell), Paragraph("Water Use in the United States", table_cell), Paragraph("USGS", table_cell), Paragraph("⚠️ Manual", table_cell), Paragraph("ScienceBase restricted access", table_cell)],
        [Paragraph("D10", table_cell), Paragraph("EJScreen Demographic/Env Data", table_cell), Paragraph("EPA / Zenodo", table_cell), Paragraph("⚠️ Manual", table_cell), Paragraph("Zenodo Cloudflare 403 block", table_cell)],
        [Paragraph("D11", table_cell), Paragraph("LEAD Energy Burden Data", table_cell), Paragraph("DOE / OpenEI", table_cell), Paragraph("✅ Verified", table_cell), Paragraph("16 County/Tract CSVs (2.78 GB)", table_cell)],
        [Paragraph("D12", table_cell), Paragraph("Hardware Lifecycle Footprints", table_cell), Paragraph("Boavizta", table_cell), Paragraph("✅ Verified", table_cell), Paragraph("2 CSV tables (735 KB)", table_cell)],
        [Paragraph("D13", table_cell), Paragraph("Hardware Impact API Archetypes", table_cell), Paragraph("Boavizta", table_cell), Paragraph("✅ Verified", table_cell), Paragraph("Model calculations (12.5 MB)", table_cell)],
    ]
    t_d = Table(d_rows, colWidths=[24, 150, 80, 80, 170])
    t_d.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0B2545')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BOTTOMPADDING', (0,0), (-1,0), 4),
        ('TOPPADDING', (0,0), (-1,0), 4),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,1), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,1), (-1,-1), 2.5),
    ]))
    story.append(t_d)
    story.append(Spacer(1, 14))

    # SECTION 2: Work Distribution Among 4 Members
    story.append(Paragraph("2. Work Distribution Across 4 Team Members", h1_style))
    story.append(Paragraph(
        "To ensure seamless execution without file conflicts, each member is assigned a primary chapter and a dedicated Jupyter notebook:",
        body_style
    ))

    # Member 1 Box
    m1_content = [
        [Paragraph("<b>MEMBER 1: Junaid — Data Ingestion & Integration Lead (Chapter 1)</b>", table_cell_bold)],
        [Paragraph("<b>Assigned Notebook:</b> <code>notebooks/01_data_ingestion_and_master_dataset.ipynb</code><br/>"
                   "<b>Primary Goal:</b> Construct the unified master dataset by integrating facility coordinates, capacity, grid emissions, and regional power characteristics.<br/>"
                   "<b>Key Tasks:</b><br/>"
                   "• Load and inspect core facility datasets (FracTracker D4 + Epoch AI D1).<br/>"
                   "• Map EPA eGRID subregions and emission rates (D8) to facility host counties.<br/>"
                   "• Join EIA-930 hourly grid generation and demand profiles (D7).<br/>"
                   "• Define ML target variables: <code>Environmental_Risk_Tier</code> (Classification) and <code>Estimated_Annual_Energy_MWh</code> (Regression).<br/>"
                   "• Output the consolidated table: <code>data/processed/master_data_centers_environmental.csv</code>.<br/>"
                   "• Write Chapter 1 of the report (Project idea, data collection, dataset description table).", table_cell)]
    ]
    t_m1 = Table(m1_content, colWidths=[504])
    t_m1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#134074')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#F0F4F8')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#134074')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_m1)
    story.append(Spacer(1, 10))

    # Member 2 Box
    m2_content = [
        [Paragraph("<b>MEMBER 2: Madhav — Data Cleaning & Quality Lead (Chapter 2)</b>", table_cell_bold)],
        [Paragraph("<b>Assigned Notebook:</b> <code>notebooks/02_data_cleaning_and_missing_values.ipynb</code><br/>"
                   "<b>Primary Goal:</b> Ensure complete data integrity, resolve missingness, and eliminate anomalies.<br/>"
                   "<b>Key Tasks:</b><br/>"
                   "• Analyze columnwise missing counts (<code>.isnull().sum()</code>).<br/>"
                   "• Generate the complete <b>missingno</b> diagnostic suite: Bar plot, Matrix plot, Heatmap, and Dendrogram.<br/>"
                   "• Identify and verify duplicate records (<code>.duplicated().sum()</code>).<br/>"
                   "• Prune redundant or extremely sparse columns (>80% missing).<br/>"
                   "• Implement domain-informed imputation (forward/backward fill, median/mode) and verify 0 remaining nulls.<br/>"
                   "• Save publication-quality figures to <code>report/figures/</code> and write Chapter 2 of the report.", table_cell)]
    ]
    t_m2 = Table(m2_content, colWidths=[504])
    t_m2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0B2545')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#0B2545')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_m2)
    story.append(Spacer(1, 10))

    # Member 3 Box
    m3_content = [
        [Paragraph("<b>MEMBER 3: Priyanshi — Visualization & Geospatial Lead (Chapter 3)</b>", table_cell_bold)],
        [Paragraph("<b>Assigned Notebook:</b> <code>notebooks/03_exploratory_data_analysis_and_visualizations.ipynb</code><br/>"
                   "<b>Primary Goal:</b> Uncover spatial, temporal, and multivariate patterns in energy and environmental impact.<br/>"
                   "<b>Key Tasks:</b><br/>"
                   "• Outlier detection via IQR boxplots with domain justification.<br/>"
                   "• Univariate & temporal distributions (yearly capacity growth, fuel mix pie charts with formatted legends).<br/>"
                   "• Geospatial analysis: Interactive <b>Folium map</b> of facilities, 2D Lat/Lon heatmaps, and KDE plots.<br/>"
                   "• Normality diagnostics via Quantile-Quantile (<b>QQ-Plots</b>) for numerical fields.<br/>"
                   "• Mixed correlation analysis (Pearson for numerical, Cramér's V for categorical).<br/>"
                   "• Deep-dive visualizations (Violin and Count plots) for highly correlated pairs (|r| > 0.7).<br/>"
                   "• Save figures to <code>report/figures/</code> and write Chapter 3 of the report.", table_cell)]
    ]
    t_m3 = Table(m3_content, colWidths=[504])
    t_m3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#134074')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#F0F4F8')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#134074')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_m3)
    story.append(Spacer(1, 10))

    # Member 4 Box
    m4_content = [
        [Paragraph("<b>MEMBER 4: Janvi — Feature Engineering & ML Lead (Chapters 4 & 5)</b>", table_cell_bold)],
        [Paragraph("<b>Assigned Notebook:</b> <code>notebooks/04_feature_engineering_and_ml_models.ipynb</code><br/>"
                   "<b>Primary Goal:</b> Engineer predictive features, select top predictors, and train ML benchmark models.<br/>"
                   "<b>Key Tasks:</b><br/>"
                   "• Feature transformation via One-Hot Encoding for categorical predictors.<br/>"
                   "• Feature selection using Random Forest feature importance scores (Top N features).<br/>"
                   "• Classification: Train Random Forest Classifier vs. SVM (70-30 train/test split, Confusion Matrix, Accuracy).<br/>"
                   "• Regression: Train Random Forest Regressor for energy consumption / emissions (R², MSE, MAE metrics).<br/>"
                   "• Build comprehensive Model Comparison Table (Table 5.1 in the IT462 format).<br/>"
                   "• Write Chapters 4 & 5 of the report.", table_cell)]
    ]
    t_m4 = Table(m4_content, colWidths=[504])
    t_m4.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0B2545')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#0B2545')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_m4)
    story.append(Spacer(1, 10))

    # Joint Work Box
    joint_content = [
        [Paragraph("<b>JOINT RESPONSIBILITIES (All 4 Members) — Chapter 6 & Final Report</b>", table_cell_bold)],
        [Paragraph("• <b>Chapter 6:</b> Synthesize environmental findings, discuss data challenges, and formulate real-world policy recommendations (siting in renewable grid corridors, water-efficient closed-loop cooling).<br/>"
                   "• <b>Report Assembly:</b> Compile all figures and tables into the official <code>IT462_2026</code> format, including Title Page, Declaration, Certificate, Group Contributions, Short Bios, and References.<br/>"
                   "• <b>Presentation:</b> Prepare final project slides for presentation to Dr. Gopinath Panda.", table_cell)]
    ]
    t_joint = Table(joint_content, colWidths=[504])
    t_joint.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2E5B88')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#EEF4F8')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#2E5B88')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_joint)
    story.append(Spacer(1, 14))

    # SECTION 3: GitHub Push & Collaboration Guide
    story.append(Paragraph("3. GitHub Integration & Step-by-Step Push Guide", h1_style))
    story.append(Paragraph(
        "<b>Important Rule for GitHub:</b> GitHub rejects any file larger than 100 MB. The raw datasets (D2 is 1 GB, D11 is 643 MB) are kept safely on your local disk and excluded via <code>.gitignore</code>. All scripts, documentation, status audits, and notebooks are tracked on GitHub.",
        body_style
    ))
    story.append(Paragraph("<b>Commands to link and push your local project to GitHub:</b>", h2_style))

    git_cmds = [
        [Paragraph("<b>Step 1: Open Terminal in Project Folder</b><br/><code>cd \"C:\\Users\\janvi\\Desktop\\EDA Project\"</code>", table_cell)],
        [Paragraph("<b>Step 2: Initialize Git Repository</b><br/><code>git init</code>", table_cell)],
        [Paragraph("<b>Step 3: Connect to Remote GitHub Repository</b><br/><code>git remote add origin https://github.com/JanviVPatel/Data-Centers-AI-Data-Centers-Environmental-Impact.git</code>", table_cell)],
        [Paragraph("<b>Step 4: Pull Existing Files from Remote</b><br/><code>git pull origin main --allow-unrelated-histories</code>", table_cell)],
        [Paragraph("<b>Step 5: Stage Code, Notebooks & Documentation (Protected by .gitignore)</b><br/><code>git add .gitignore README.md src/ notebooks/ report/ EDA\\ Data/dataset_download_status.md</code>", table_cell)],
        [Paragraph("<b>Step 6: Commit and Push to Main Branch</b><br/><code>git commit -m \"Initialize IT462 EDA project structure, modular notebooks, and download status\"</code><br/><code>git push -u origin main</code>", table_cell)]
    ]
    t_git = Table(git_cmds, colWidths=[504])
    t_git.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#D0D7DE')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_git)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully built: {PDF_PATH}")

if __name__ == "__main__":
    build_pdf()
