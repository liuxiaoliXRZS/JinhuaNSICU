# JinhuaNSICU
**JinhuaNSICU**  is a single-center, bilingual (Chinese and English), and open shared database focused on neurosurgery patients. This database has been filtered, cleaned, and de-identified, recording a variety of rich clinical information throughout the entire hospital stay of patients admitted to the NSICU. And it can be publicly acquired at the [China National Center for Bioinformation](https://ngdc.cncb.ac.cn/omix/release/OMIX011033).


### Repository Structure

- **icu_details.py**
    This script processes hospital admission records and ICU treatment data to generate a summary table containing key metrics such as hospital length of stay (LOS), ICU treatment duration, and patient details.
- **statistic_admission_data.py**
    This script analyzes admission data to calculate statistics about multiple admissions and time spans.
- **./paperFigure**
	consists of all figures code in the paper.
	- **figure_boxplot.py**
		plot boxplots of hospital stay lengths, combining data from different datasets. (Paper Figure 3)
	- **figure_length_of_hosp.py**
		generates three sets of density plots to visualize the distribution of hospital stay lengths from different datasets. (Paper Figure 4)
	- **figure_patient.py**
		generates a comprehensive visualization of a patient's medical data, including vital signs, laboratory tests, medications, surgeries, and examinations. (Paper Figure 2)
- **./utils**
	- **cal_icu_day.py**
		Calculate the total ICU time for each hospital admission (hadm_id)
	- **extract.py**
		Process medical records data
	- **func.py**
		Some useful functions
    - **herbal_medicine.py**
		Analyzes the distribution of herbal medicine doses for a specific set of herbs using visualizations.
    - **tableone.py**
		Generate a TableOne object from a dataset and save it to an Excel file.
- **./JinhuaNSICU_building**
	consist of files of building the JinhuaNSICU dataset.
- **./surgery_analysis_mimiciv.sql**
	This script is able to extract patient basic information, length of hospital stay, and other content from the MIMIC-IV database.
