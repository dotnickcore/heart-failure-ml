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
  - **Value 0**: Normal
  - **Value 1**: Having ST-T wave abnormality
  - **Value 2**: Showing probable or definite left ventricular hypertrophy
- **thalach**: Maximum heart rate achieved
- **exang**: Exercise induced angina (1 = Yes; 0 = No)
- **ca**: Number of major vessels colored by fluoroscopy (0-3)
- **target**: Diagnosis target
  - **0**: Less chance of heart attack
  - **1**: More chance of heart attack

