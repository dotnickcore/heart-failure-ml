# Heart Attack Machine Learning Analysis
## Background
### What is the human heart and what is a heart attack?
The human heart is a powerful pump. A heart attack (myocardial infarction) happens when a blocked coronary artery prevents oxygenated blood from reaching a section of the heart muscle, leading to tissue death.

## About the data
- **Age**: Age of the patient
- **Sex**: Sex of the patient (1 = male; 0 = female)
- **cp**: Chest Pain type
  - **Value 0**: Typical angina (The standard, recognizable pain caused by a clogged heart artery, i.e. pressure or squeezing in the chest)
  - **Value 1**: Atypical angina (Chest pain that feels unusual or different from the standard type, i.e. sharp or off-center pain)
  - **Value 2**: Non-anginal pain (Pain that is probably not related to a heart problem, likely from muscles, acid reflux, etc)
  - **Value 3**: Asymptomatic (The patient does not feel any chest pain at all)
- **trtbps**: Resting blood pressure (in mm Hg)
- **chol**: Cholesterol in mg/dl
- **fbs**: Fasting blood sugar > 120 mg/dl (1 = True; 0 = False)
- **rest_ecg**: Resting electrocardiographic results
  - **Value 0**: Normal (A standard, healthy reading)
  - **Value 1**: Having ST-T wave abnormality (An irregularity in the reading that can be a sign of heart strain or lack of oxygen)
  - **Value 2**: Showing probable or definite left ventricular hypertrophy (Indicates the main heart muscle is enlarged, which makes it harder to pump blood effectively)
- **thalach**: Maximum heart rate achieved
- **exang**: Exercise induced angina (1 = Yes; 0 = No)
- **oldpeak**: ST depression induced by exercise relative to rest
- **slp**: The slope of the peak exercise st segment. An ST segment is a brief period between when the heart's lower chambers (ventricles) have finished contracting and when they start to relax and reset for the next beat.
  - **Value 0**: Downsloping
  - **Value 1**: Flat
  - **Value 2**: Upsloping
- **ca**: Number of major vessels colored by fluoroscopy (0-3)
- **thall**: Results from a thallium stress test, indicating the severity or presence of a condition, otherwise to show how well blood flows to your heart, both at rest and under stress.
  - **Value 1**: Fixed Deflect
  - **Value 2**: Normal
  - **Value 3**: Reversable Deflect
- **target**: Diagnosis target
  - **0**: Less chance of heart attack
  - **1**: More chance of heart attack
## Libraries used
- **Numpy**: A fundamental package for scientific computing in Python. It provides the core data structures and operations for handling numerical data.
- **Pandas**: A fast, powerful, and flexible library built on top of NumPy, designed specifically for data manipulation and analysis.


