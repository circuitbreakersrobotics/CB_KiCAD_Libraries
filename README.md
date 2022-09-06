![Version](https://img.shields.io/badge/COMPONESNTS-330-yellow?style=for-the-badge)   ![PLATFORM](https://img.shields.io/badge/PLATFORM-KiCAD-informational?style=for-the-badge&?link=https://www.kicad.org/=https://www.kicad.org/)   ![Version](https://img.shields.io/badge/Version-v0.0.4-success?style=for-the-badge) <a href="https://www.youtube.com/c/CircuitBreakersRobotics"><img src="https://img.shields.io/badge/YouTube-red?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube Badge"/></a>

# **CircuitBreakers KiCAD Libraries**

![Final](./resources/home.png)

##  **Introduction**
---

Circuit Breaker Robotics KiCAD library pack is a collection of common electronic components libraries for the free and open-source KiCAD PCB design software. The goal of Circuit Breaker KiCAD Libraries is to provide a user-friendly library package for beginners. Components like resistors and capacitors are name base on the values like 10k,100ohm, 22uF… So users can directly search for the value and directly add it to their design. Most of the footprints and the 3D models are directly linked to KiCAD’s default libraries. So users can still use KiCAD,s official footprints, and 3D models.  

## **Requirements**
---
- You need to have a KiCAD version 6 or above. If not, install the latest KiCAD version from <a href="https://www.kicad.org/download/">here</a>.

- Required to have default(official) KiCAD libraries installed in KiCAD. Because some symbols in CB KiCAD Libraries are linked to KiCAD default libraries.

- Need to have 200MB of disk space.

## **How to install 📜**
---

The CB KiCAD libraries can be installed through **📦 PCM(Pluging and Content Manager)** in KiCAD manually.

1. First you need to download the latest release vision of the library pack. Click below to download the latest release vision.


    ### **+------------------------------------------------------------------------+**
     ##         **📂Download -> <a href="https://github.com/circuitbreakersrobotics/CB_KiCAD_Libraries/releases/download/v0.0.4/CB_KiCAD_Libraries_v0.1.zip">CB_KiCAD_Libraries_v0.1</a>**
    ### **+------------------------------------------------------------------------+**

  ![footprints](./videos/gif_01.gif) 

2. After downloading the package, open KiCAD and launch the PCM.

     ![PCM](./videos/PCM.png) 

3. Click on the option "Install from File" and select the downloaded zip file. Then the library files will be extracted into the KiCAD third-party library directories. 

     ![PCM](./videos/install.png) 


  ![footprints](https://raw.githubusercontent.com/circuitbreakersrobotics/CB_KiCAD_Libraries/main/videos/gif_02.gif) 


4. After successfully installing the libraries we need to manually update symbol and footprint library tables. To do that go to **preference > 📚manage symbol libraries** and select the **global library** section. Then click the file icon at the bottom and navigate to the following location according to your operating system.

      ![Symbole Lib Add](./videos/SymLibAdd.png) 

**Windows ->** 

|__`📄Documents > KiCad > 6.0 > 3rdparty > symbols > com_github_circuitbreakersrobotics_CB-KiCAD-Libraries`__ |  

    
5. Then select all the symbols libraries in that directory and click **open**. After adding the symbol files to the library table click **OK** to close the symbol library manage window.

     ![Selecting Symbole](./videos/SelectingSymLib.png)

6. To add footprint libraries go to **preference > 📚manage footprint libraries** and select the **global library** section. Then click the file icon at the bottom and navigate to the following location according to your operating system. 

     ![FooprintLibAdd](./videos/FooprintLibAdd.png) 


 **Windows ->** 

 | __`📄Documents > KiCad > 6.0 > 3rdparty > footprints > com_github_circuitbreakersrobotics_CB-KiCAD-Libraries`__ |

 

7. Then select all the footprint folders in that directory and click **Select Floder** . After adding the footprint folders to the library table click **OK** to close the footprintl library manage window.

     ![Select footprints](./videos/SelectFootprintLib.png) 

To check whether all the symbol libraries are installed correctly, open the schematic editor and go to Add Symbole command. Then scroll through the list of libraries and see whether the following libraries are in the list. 

- CB_3Dmodels
- CB_Breakout_Boards
- CB_Capacitors
- CB_Connectors
- CB_DevelopmentBoards
- CB_Devices
- CB_Jumpers_THT
- CB_Mechanical
- CB_PinHeaders
- CB_Resistors
- CB_Transistors


![Symbole Chooser](./videos/CBSymboleLibs.png) 

To check whether all the footprint libraries are installed correctly. Go to the Footprint Editor and find similar libraries to symbol library names in the Library panel as shown in the following image. 

![Symbole Chooser](./videos/CBFootprintLib.png) 

If all the libraries are installed correctly you can browse through the components in the Circuit breakers KiCAD libraries. To learn about the components in the CB KiCAD Library pack see what’s in this library section. 

##  **What’s in this library pack?**
---


KiCAD Library pack was created to make the adding components to the project easy. This library pack contains value-based component libraries. For example, if you need to add a 10k resistor to the schematic just type 10k on the search bar and you will get a 10k resistor with the value on it.  Just like that, we can search for common capacitors and crystal oscillators based on their values. When selecting footprints to the symbol only the commonly used packages are filtered. Which makes the footprint selection process easy. If you cannot find the value or footprint you are looking for, You add the common component symbol from the default KiCAD libraries and change the value and the footprint accordingly. 

![Resistor Symbole](./videos/ResistorSym.png) 

CB KiCAD libraries contain symbols for some common connectors like Pinheaders male and female,  JST connectors, and Terminal Block connectors. This allows the user to search the name directly and get the symbol and the footprint need for the project. 

CB KiCAD also contains some development board and breakout board libraries with 3D models for some of the packages.  

All the components in theCB  KiCAD Library are listaed below. 


<div id="CB KiCAD Library List" align="left">
 <table>
   <thead>
    <tr>
     <th colspan="3" rowspan="1"><b>CB KiCAD Library List</b></th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td><strong>CB_Devices</strong></td>
     <td>
     <ul>
       <li><p>Buzzer_5v</p></li>
       <li><p>Crystal_8MHz - 24MHz</p></li>
       <li><p>Crystal 32.768kHz</p></li>
       <li><p>IC DIP Package 8,14,16</p></li>
       <li><p>LED 5mm, 3mm, 8mm, 10mm</p></li>
        <li><p>Push Button</p></li>
       <li><p>Potentiometer RM065, 3362P, RK163</p></li>
       <li><p>Resistor 0.5W, 1W, 5W, 10W</p></li>
       <p>  </p>
    </tr>
    <tr>
     <td><strong>CB_Capacitors</strong></td>
     <td>
     <ul>
       <li><p>1uF to 4700uF</p></li>
    </tr>
    <tr>
     <td><strong>CB_Resistors</strong></td>
     <td>
     <ul>
       <li><p>0 ohm to 10M</p></li>
    </tr>
    <tr>
     <td><strong>CB_Transistors</strong></td>
     <td>
     <ul>
       <li><p>BC108</p></li>
       <li><p>C828</p></li>
       <li><p>D313</p></li>
       <li><p>D400 🆕</p></li>
    </tr>
    <tr>
     <td><strong>CB_Connectors</strong></td>
     <td>
     <ul>
       <li><p>JST Pin 02 -10</p></li>
       <li><p>Servo Ports pin 01 - 08</p></li>
    </tr>
    <tr>
    <td><strong>CB_PinHeaders</strong></td>
     <td>
     <ul>
       <li><p>Pinheaders Male 1x1 - 1x20</p></li>
       <li><p>Pinheaders Female 1x1 - 1x20</p></li>
       <li><p>Pinheaders Male 2x1 - 1x5</p></li>
       <li><p>Pinheaders Female 2x1 - 1x5</p></li>
    </tr>
    <tr>
    <td><strong>CB_Screw_Terminal</strong></td>
     <td>
     <ul>
       <li><p>Screw Terminal P5.00mm Pin  2 - 9</p></li>
       <li><p>Screw Terminal P3.5mm Pin  2 - 9</p></li>
    </tr>
    <tr>
    <td><strong>CB_Jumpers_THT</strong></td>
     <td>
     <ul>
       <li><p>Jumpers from 10mm - 120mm</p></li>
    </tr>
    <tr>
     <td><strong>CB_DevelopmentBoards</strong></td>
     <td>
     <ul>
       <li><p>Arduino Pro Mini</p></li>
       <li><p>ESP32 CAM</p></li>
       <li><p>ESP32 DevKit V1 DOIT 30GPIOs 🆕</p></li>
       <li><p>ESP32 DevKit V1 DOIT 32GPIOs 🆕</p></li>
       <li><p>Lolin NodeMCU ESP8266 V3</p></li>
       <li><p>Rasberry Pi Pico</p></li>
       <li><p>Blue Pill DevBoard</p></li>   
    </tr>
    <tr>
         <td><strong>CB_Breakout_Boards</strong></td>
     <td>
     <ul>
       <li><p>A4988</p></li>
       <li><p>HC-05 Bluetooth Module🆕</p></li>
       <li><p>HC-06 Bluetooth Module</p></li>
       <li><p>HC SR04 Ultrasonic Sensor</p></li>
       <li><p>LCD 16x4</p></li>
       <li><p>MPU6050🆕</p></li>
       <li><p>PIR Sensor</p></li>
    </tr>
     </tbody>
  </table>
</div>
