# Eye Clinic Database Documentation

This documentation outlines the eye examinations and tests to be stored in the `AllCase.db` database. Each section details the types of exams, history fields, and related tests, specifying what each includes.

## Table of Contents
- [Patient Information](#patient-information)
- [Patient History](#patient-history)
- [Examinations and Tests](#examinations-and-tests)
  - [Pupil Tests](#pupil-tests)
  - [Visual Acuity Tests](#visual-acuity-tests)
  - [Refraction Tests](#refraction-tests)
  - [Other Eye Tests](#other-eye-tests)

---

## Patient Information
- **ID**: Unique identifier for each patient.
- **Name**: Full name of the patient.
- **Age**: Patient’s age at the time of the exam.
- **Gender**: Gender of the patient.

---

## Patient History

Patient history is divided into specific fields to capture detailed information about symptoms, duration, frequency, and other relevant factors.

### Fields:
- **Chief Complaint**: Primary reason for the visit.
- **Duration**: How long the symptom(s) or condition has been present.
- **Regularity**: Whether symptoms are constant or intermittent.
- **Frequency**: How often symptoms occur (e.g., daily, weekly).
- **Associated Signs or Symptoms**: Other symptoms accompanying the main complaint.
- **Location**: Specific area affected (e.g., right eye, left eye).
- **Laterality**: Whether the issue affects one eye or both.
- **Onset**: Description of how the condition started (e.g., sudden, gradual).
- **Pain Level**: Pain intensity rating (e.g., 0-10 scale).
- **Prescription Medication**: Any medications prescribed and related details.
- **Exacerbating Factors**: Factors that worsen the condition.
- **Severity**: Severity of the condition, typically rated from mild to severe.

---

## Examinations and Tests

### Pupil Tests
- **Direct Light Response**: Records pupil reaction to direct light.
- **Consensual Light Response**: Records pupil reaction in the opposite eye.
- **Swinging Flashlight Test**: Checks for afferent pupillary defects.
- **Accommodation Response**: Tests pupil constriction with near-focus.

### Visual Acuity Tests
- **Distance Visual Acuity**: Measured in Snellen or decimal format.
- **Near Visual Acuity**: Tested at a closer distance, typically with reading charts.
- **Color Vision**: Ishihara or other color vision tests.

### Refraction Tests
- **Auto-Refraction**: Machine-measured refraction data.
- **Manual Refraction**: Subjective refraction findings from a phoropter or trial lenses.
- **Cycloplegic Refraction**: Refraction under cycloplegia to prevent accommodation.

### Other Eye Tests
- **Tonometry**: Measures intraocular pressure.
- **Ophthalmoscopy**: Examination of the retina, optic disc, and blood vessels.
- **Slit Lamp Exam**: Detailed inspection of anterior segment structures.
- **Fundus Photography**: Captures images of the retina for documentation.
- **Visual Field Test**: Assesses peripheral vision loss.
- **OCT (Optical Coherence Tomography)**: Imaging of retinal layers.

---

## Data Entry Format
Each test result should be stored with standardized units and notes as necessary, e.g.,:
- **Visual Acuity**: Enter in Snellen (e.g., 20/20) or decimal (e.g., 1.0).
- **Pupil Test Results**: Record as “Normal” or specify any abnormal findings.
- **Tonometry**: Measured in mmHg.

## Additional Notes
- **Images**: Where possible, include paths to images, such as fundus photographs or OCT scans, for visual documentation.
- **Graphical Data**: Include paths to graphs (e.g., visual field graphs) if available.
