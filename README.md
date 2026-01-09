<a name="readme-top"></a>

<!-- HEADER-->
<br />
<div align="center">
   <a href="#">
    <img src="https://0.academia-photos.com/13780162/10171376/11350231/s200_katherine.castillo_panduro.jpg" alt="Logo" width="357" height="162">
  </a>
  
  <h3 align="center">Questract (Prototype)</h3>

  <p align="center">
    <strong>Optical Mark Recognition (OMR) Engine with Computer Vision</strong>
    <br />
    <em>An engineering study on digitizing physical questionnaires into JSON.</em>
  </p>
</div>

<br />

> [!WARNING] > **PROJECT ARCHIVED** > <br />
> This project was developed in **September 2025** and is now **Read-Only**.
> It was built to solve a specific research bottleneck but was eventually halted due to a pivot in the research methodology. The code remains available as a case study in **Coordinate Mapping** and **Computer Vision** algorithms.

<br />

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#context--the-problem">Context & The Problem</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#technical-architecture--future-directions">Technical Architecture & Future Directions</a>
      <ul>
        <li><a href="#core-implementation">Core Implementation</a></li>
        <li><a href="#explored-solutions">Explored Solutions</a></li>
      </ul>
    </li>
    <li><a href="#documentations">Documentations</a></li>
  </ol>
</details>

<!-- BODY -->

## Context & The Problem

**Questract** was born from a real-world data entry bottleneck.

A Psychology researcher was conducting a study on a sensitive topic (**contraceptive usage**) and required physical paper forms to ensure respondent privacy and comfort. This resulted in over **100+ handwritten pages** that needed to be digitized.

Watching the manual entry process—moving data from paper to Excel one by one—I realized this was a scalability problem. The hypothesis was simple: **Since the form layout is static (template-based), we should be able to map the coordinates once and automate the reading process.**

### The Technical Pivot (Why it stopped)

<a href="#">
   <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGNtN3h6Z2N0Nm14eG5hcjNrZ29sZTZpaGt1d3NpOHd4dXR6cHY2MyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/LAKIIRqtM1dqE/giphy.gif" alt="Logo" width="357" height="162">
</a>
  
The prototype successfully processed flat-bed scans using a JSON coordinate blueprint. However, in real-world scenarios, mobile photography introduced **geometric distortions** (paper curling, perspective warping, and lighting shadows).

While I researched advanced solutions like <a href="https://openaccess.thecvf.com/content_ICCV_2019/papers/Das_DewarpNet_Single-Image_Document_Unwarping_With_Stacked_3D_and_2D_Regression_ICCV_2019_paper.pdf">
_DewarpNet (Single-Image Document Unwarping)_
</a> to flatten the images digitally, the research timeline was tight. The researcher eventually pivoted the data collection method, removing the need for this tool. I decided to archive the project here rather than leaving it unfinished, documenting the "Coordinate Blueprint" logic which remains a valid solution for flat-scan OMR.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- [![Python][Python]][Python-url]
- [![OpenCV][OpenCV]][OpenCV-url]
- [![Streamlit][Streamlit]][Streamlit-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Technical Architecture & Future Directions

### Core Implementation

This repository demonstrates three key engineering concepts used to solve the OMR problem:

**1. JSON-Based Coordinate Blueprint**

Instead of hardcoding pixel values, the system relies on a **Config-Driven Architecture**. The layout of the questionnaire is defined in a separate JSON file (`generated_config.json`). This makes the engine agnostic; it doesn't care _what_ the form asks, it only cares _where_ the boxes are.

**2. Automated Coordinate Discovery**

Mapping hundreds of checkboxes manually is tedious. I built an internal tool (`scripts/automated_finder.py`) that utilizes **Contour Detection** to scan a blank template. It automatically identifies square shapes, filters them by aspect ratio, and generates the coordinate JSON blueprint in seconds.

**3. Adaptive Thresholding Logic**

The engine doesn't just look for black pixels. It calculates the **pixel density** within a specific Region of Interest (ROI).

- It handles variations in pen thickness and scan contrast.
- It distinguishes between "noise" (scanner dust) and a valid "check mark" using dynamic thresholding.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Explored Solutions

During development, I researched several advanced techniques to handle real-world photo distortions. These weren't implemented due to timeline constraints and the research methodology pivot, but they represent viable next steps for similar projects:

| Solution                             | Purpose                                                                     | Implementation Complexity | Trade-offs                                                                                |
| ------------------------------------ | --------------------------------------------------------------------------- | ------------------------- | ----------------------------------------------------------------------------------------- |
| **ArUco Marker Registration**        | Print fiducial markers at form corners for automatic perspective correction | Medium                    | ✓ Reliable detection<br>✓ Handles severe warping<br>✘ Requires modifying form templates   |
| **Edge-Based Perspective Transform** | Detect form boundaries using Hough Line Transform to unwarp images          | High                      | ✓ Works on existing forms<br>✘ Sensitive to poor lighting<br>✘ Complex edge case handling |
| **Pre-Processing Quality Gates**     | Reject blurry/dark images before processing using Laplacian variance checks | Low                       | ✓ Better user feedback<br>✓ Prevents garbage output<br>✘ Adds validation overhead         |

The core challenge—**geometric distortion from mobile photography**—would have required perspective transformation algorithms or deep learning-based document dewarping (e.g., [DewarpNet](https://openaccess.thecvf.com/content_ICCV_2019/papers/Das_DewarpNet_Single-Image_Document_Unwarping_With_Stacked_3D_and_2D_Regression_ICCV_2019_paper.pdf)). While technically solvable, the research timeline shift made these enhancements unnecessary.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Documentations

Below is the visualization of the engine in action before the project was archived.

![Demo Questract 1](https://i.postimg.cc/C1ybfY1N/Screenshot-2026-01-09-at-15-54-40.png)
![Demo Questract 2](https://i.postimg.cc/DwrhKPXY/Screenshot-2026-01-09-at-15-54-47.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FOOTER -->
<br />
<p align="center">
  <small>
    Developed by 
    <a href="https://www.linkedin.com/in/firyan-fatih-fadilah">
      Firyan Fatih Fadilah
    </a>
    as a Mini-Research Project.
  </small>
</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[Python]: https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python
[Python-url]: https://www.python.org
[OpenCV]: https://img.shields.io/badge/OpenCV-000000?style=for-the-badge&logo=opencv
[OpenCV-url]: https://opencv.org/
[Streamlit]: https://img.shields.io/badge/Streamlit-000000?style=for-the-badge&logo=Streamlit
[Streamlit-url]: https://streamlit.io/
