# IKR Security Systems
This project takes a radically different approach to home security systems while incorportaing the [Edge Computing](https://en.wikipedia.org/wiki/Edge_computing) paradigm, the latest AI optimized hardware from NVIDIA([Jetson Nano](https://developer.nvidia.com/embedded/jetson-nano-developer-kit)), and Computer Vision(CV) models to ensure efficiency and security.

<img width="751" alt="Screen Shot 2023-06-06 at 12 25 11 AM" src="https://github.com/kartikgulia/IKR-Security-Systems/assets/44033533/e7d14ade-2153-40de-a30d-3c5c530a65e2">

---

**Developers:** Isean Bhanot, Kartik Gulia, Ryan Lee

---

## Description
Our product begins with ensuring a quick and secure entry of an individual, by recognizing a user defined hand signal, to allow them access into the house using home security system. Once the proper individual is allowed inside, we monitor the number of people inside the house to ensure there aren't any intruders coming in with the allowed individual. We also monitor the number of people inside the house, after an individual is safely insde, in order to limit the amount of people inside the house at one time. 

The color coding for the diagram above it as follow: _**Green**_ refers to sensors or actuators; _**Red**_ referes to an [Edge device](https://en.wikipedia.org/wiki/Edge_device), a computational and/or power constrained device that is closest to the sources of data; _**Yellow**_ refers to the [Fog layer](https://en.wikipedia.org/wiki/Fog_computing), the intermediate or communication layer between the cloud and devices; and _**Blue**_ refers to the [Cloud layer](https://en.wikipedia.org/wiki/Cloud_storage), where large amounts of storage and some computation is offloaded to.

## Hardware
- **NVIDA Jetson Nano 4G** - Uses Computer Vision to detect the number of people in a room and sends that data to the 2G Jetson Nano. This device is considered an Edge Device.
- **NVIDA Jetson Nano 2G** - Uses Computer Vision to understand the hand signal a person is making(ex. fist, peace, stop...) and sending that data, along with data passed to it from the 4G Jetson Nano, to the Cloud. This device is considered an Edge and Fog Device.
- **Arduino Uno** - Uses C++ code to simulate the locking mechanism of a door. This was used to test our code in a real-world setting.
- **2 x 1080p USB Cameras** - One is pointed outward, to detect hand signals, while the other is pointed into the house to detect the number of people in the house.

## Software
- **Python** - Neural Network based Computer Vision(CV) Model for detecting hand gestures.
- **Python** - HOG(Histogram of Oriented Gradients) Computer Vision Model for detecting number of people in a room.
- **C++** - Embedded system(Arduino) code to interface with Jetson Nano's GPIO pins and simulate a house our product is protecting.
- **Google Cloud: Cloud Pub/Sub API** - Provided secure communication for sending processed data and commands between the Jetson Nano and the Cloud.
- **Google Cloud: BigQuery API** - Getting streamed data from the Cloud Pub/Sub API and processing it into command for the Cloud Pub/Sub API to send back to the devices.

## Documentation/Development
Presentation - [https://docs.google.com/presentation/d/1pqVk83XJ9n7nyiAHr2vTr5-TVuU_JEAqzoBZaLbjyEo/edit?usp=sharing](https://docs.google.com/presentation/d/1lxYeCWnt3oS_AHh2rv0MB2TIrI1ZfRE_RhjPCvxZjRA/edit?usp=sharing). <br>
Phase 1 - https://drive.google.com/file/d/1-sivq8wsVOF8uHiouNWtOJpHUIPxzj0u/view?usp=sharing <br>
Phase 2 - https://drive.google.com/file/d/1LmbUpyhvuDfTdb28KLyF1YDDbZ_Je44w/view?usp=sharing <br>
Phase 3(Final Report) - https://drive.google.com/file/d/1PHDZYVXvOXPEXAH7yYCuVqq1gU_o4-NV/view?usp=sharing. <br>

