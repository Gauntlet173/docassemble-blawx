# docassemble-blawx
A module for connecting Docassemble interviews to Blawx.com

## Alpha Software
Blawx.com and the Blawx.com Reasoner are currently free-to-use alpha-version software.
They should not be used for production purposes. The functionality of Blawx.com and
the Blawx.com reasoner may change over time without notice. Code generated in earlier
versions of the Alpha software may not work in later versions. Use at your own risk.

## Installation
Go into the packages section of your docassemble server and enter the github address for
this package.  See the [docassemble documentation](https://docassemble.org/docs)
for details.

## Usage
1. Include docassemble.blawx as a module in your interview.
```
modules:
  - docassemble.blawx
```
2. Create a object with the type Blawx in your interview.
```
objects:
  - reasoner: Blawx
```
3. Save your Blawx source code to a file, and upload that file to the static folder of 
   your docassemble server.
   See the [docassemble documentation](https://docassemble.org/docs) for details.
4. Call the ask() method of the Blawx object you created.
```
  answer = reasoner.ask('filename.blawx')
```
5. Use the output of the ask() method to read the answer from the Blawx.com Reasoner.

## The Docassemble Data Structure
When you use this module, the interview data is sent to the Blawx Reasoner, where it is
converted for use in Blawx Code.  The docassemble interview data will be converted
into a "data dictionary", with "data" as the name of the root object.

For example, if you have a variable named "foo", that will appear in Blawx as an object
named "data", with a data property named "foo", set to the value of "foo".

Nested objects, such as docassemble's DAList and elements, will be represented as
nested data dictionaries. Only the root of the dictionary is a named object.

## The Blawx Response Structure
Blawx's response is in the following format:
```
{
  'main': 'Yes' (or 'No'),
  'answers': {
    '1': {
      'variable': value,
      ...
    }
    ...
  }
}
```
If the query is a yes/no query, only 'main' will be returned. If the query is a search
and no results are returned, only 'main' will be returned with a value of 'No'.
If it is a search and there are results, 'main' and 'answers' will be included.

## More Info
See the [Learn section on Blawx.com](https://www.blawx.com/learn) for more details.

Blawx also has a public [Slack server](https://blawx.slack.com).