![Version](https://img.shields.io/badge/COMPONESNTS-322-yellow?style=for-the-badge)   ![PLATFORM](https://img.shields.io/badge/PLATFORM-KiCAD-informational?style=for-the-badge)   ![Version](https://img.shields.io/badge/Version-v0.0.3-success?style=for-the-badge)

# **CircuitBreakers KiCAD Libraries**

![Final](./resources/home.png)

##  **Introduction**
---

Circuit Breaker Robotics KiCAD library pack is a collection of common electronic components libraries for the free and open-source KiCAD PCB design software. The goal of Circuit Breaker KiCAD Libraries is to provide a user-friendly library package for beginners. Components like resistors and capacitors are name base on the values like 10k,100ohm, 22uF… So users can directly search for the value and directly add it to their design. Most of the footprints and the 3D models are directly linked to KiCAD’s default libraries. So users can still use KiCAD,s official footprints, and 3D models.  

## **How to install 📜**
---

The CB KiCAD libraries can be installed through **📦 PCM(Pluging and Content Manager)** in KiCAD manually.

1. First you need to download the latest release vision of the library pack. Click below to download the latest release vision.


    ### **+------------------------------------------------------------------------+**
     ##         **📂Download -> <a href="https://github.com/circuitbreakersrobotics/CB_KiCAD_Libraries/releases/download/v0.0.3/CB_KiCAD_Libraries_v0.0.3.zip">CB_KiCAD_Libraries_v0.0.3</a>**
    ### **+------------------------------------------------------------------------+**

  ![footprints](./videos/gif_01.gif) 

2. After downloading the package, open KiCAD and launch the PCM.

3. Click on the option "Install from File" and select the downloaded zip file. Then the library files will be extracted into the KiCAD third-party library directories. 

 ![footprints](./videos/gif_02.gif) 

4. After successfully installing the libraries we need to manually update symbol and footprint library tables. To do that go to **preference > 📚manage symbol libraries** and select the **global library** section. Then click the file icon at the bottom and navigate to the following location according to your operating system.

**Windows ->** 

|__`📄Documents > KiCad > 6.0 > 3rdparty > symbols > com_github_circuitbreakersrobotics_CB-KiCAD-Libraries`__ |  

    
5. Then select all the symbols libraries in that directory and click **open**. After adding the symbol files to the library table click **OK** to close the symbol library manage window.

     ![symbols](./videos/gif_03.gif)

6. To add footprint libraries go to **preference > 📚manage footprint libraries** and select the **global library** section. Then click the file icon at the bottom and navigate to the following location according to your operating system. 




 **Windows ->** 

 | __`📄Documents > KiCad > 6.0 > 3rdparty > footprints > com_github_circuitbreakersrobotics_CB-KiCAD-Libraries`__ |

 

7. Then select all the footprint folders in that directory and click **Select Foder** . After adding the footprint folders to the library table click **OK** to close the footprintl library manage window.

     ![footprints](./videos/gif_04.gif) 
