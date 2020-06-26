# Inventorygen

CLI script to generate an inventory file from the data to be processed with the [Namalysator](https://github.com/natliblux/Namalysator)

## Setup

Inventorygen requires python 3.7 and should be installed in a virtual environment.

```bash
pip install .
```

## Usage
Inventorygen will install the CLI script and requires a configuration file is required.
If it is not specified, it will look for a file named ```conf.yml``` in the current directory.
```bash
usage: inventorygen [-h] [-c CONFIG_FILE] -d DATA_PATH [-p PROJECT_NAME] -o
                    OUTPUT_FILE
```

The script will then parse the data directory recursively using ```os.walk``` looking for TIF files. 
Each directory containing at least one TIF image will be considered as a document entry in the inventory file.
The script will then extract the number of pages and date of the document.
The date is used to determine which section (```default``` or ```yearconf``` interval) of the configuration file should be used for other to apply other settings.
Logs are generated in log.inventorygen

## Configuration

* ```project:``` specify the project name
* ```datapath:``` Directory containing data to parse. The basename of this path is used as the journal name. 
* ```outputfile:``` generated inventory file

* ```default:``` Configuration section used if the date of a document couldn't be parsed or doesn't fall in a section specified in ```yearconf```.
* ```yearconf:``` List of configuration section specifying different parameters for different date intervals specified with ```from``` and ```to```.

```yaml
project: ExampleProject
datapath: "/path/to/data"
outputfile: inventory.xml
default: # Default attributes used for issues with no matching yearconf
  type: Newspaper
  callNumber: callNumberDef
  title: TitleDef
  titleCollection: Title CollectionDef
  subTitle: subTitleDef
  printer: printerDef
  publisher: publisherDef
  languages: [fr, de]

yearconf: # Specify attributes for a given interval
  - from: 1866-01-01
    to: 1989-12-31
    type: Newspaper
    callNumber: callNumber1
    title: Title1
    titleCollection: Title Collection1
    subTitle: subTitle1
    printer: printer1
    publisher: publisher1
    languages: [fr, de]
  - from: 1990-01-01
    to: 1990-12-31
    type: Newspaper
    callNumber: callNumber2
    title: Title2
    titleCollection: Title Collection2
    subTitle: subTitle2
    printer: printer2
    publisher: publisher2
    languages: [en]
 ```
