# Certificate Generator
A set of programs to help you generate and email certificates automatically

## Guide
* Replace the file `template.png` with your own design template.
* Make sure to modify the pixel values accordingly for the draw function in all the python scripts.
* Make final.csv with the same format as test.csv file.
* Insert your own email credentials in the .env example file

## Scripts
* [main.py](https://github.com/ujjujjuj/Certificate-Generator/blob/master/main.py) - get users from final.csv, generate and email certificates all at once
* [individual.py](https://github.com/ujjujjuj/Certificate-Generator/blob/master/individual.py) - generate and email certificate to one user only
* [sample.py](https://github.com/ujjujjuj/Certificate-Generator/blob/master/main.py) - generate certificates and save them to img/ to see how they will turn out
