# WinSCP

## Installation

* You need to download and install **WinSCP** software from this link: 
https://winscp.net/eng/download.php
  
* After installation is complete, you can register the connection to the FTP server.
  
## Register your Lizmap server

* 1 By email, you should have received the login credentials to the FTP server.
* 2 Open **WinSCP**.
* 3 The panel for adding a new connection opens automatically when the software is opened for the first time.
  Otherwise, click on the button `New session` located at the top left of the window.

![WinSCP](./media/ftp_winscp_1.jpg)

* 4 **New site**

![WinSCP](./media/ftp_winscp_2.jpg)

* 5 Complete the information:
    * **1**: File protocol: `FTP`
    * **2**: Encryption: `Explicit TSL / SSL encryption`
    * **3**: Hostname: The FTP server received by email
    * **4**: Port Number: `21`
    * **5**: Username: The username received by email
    * **6**: Password: The password received by email

![WinSCP](./media/ftp_winscp_3.jpg)

* 6 Click on save to save the new site:
    * **1**: Save the session under: Site name, ex: Lizmap
    * **2**: Save password: You can check the box if you wish
    * **3**: Create a shortcut on the desktop: Allows direct access to the site via a shortcut on your office

![WinSCP](./media/ftp_winscp_4.jpg)

* 7 To connect to your new site go to the `Session` tab then` Sites` and click on your site.

![WinSCP](./media/ftp_winscp_5.jpg)

* 8 You should have a screen similar to this: 

![WinSCP](./media/ftp_winscp_6.jpg)

* Description of the user interface : 
    * On the left, your computer
    * On the right, the server

* With a **drag&drop**, we can copy files from the computer to the server.

## File tree

On the server, **always** in the `qgis`, we are going to create directories which will be a Lizmap theme.

Then, in your Lizmap panel administration, you need to add the directory.

For instance :

```bash
/
├── qgis
│   ├── forest
│   │   ├── jungle.qgs
│   │   ├── jungle.qgs.cfg
│   │   └── media
│   │       └── logo.png
│   ├── social
│   └── urban
│       ├── populated_places.qgs
│       ├── populated_places.qgs.cfg
│       ├── urban_project.qgs
│       └── urban_project.qgs.cfg
└── web
```
