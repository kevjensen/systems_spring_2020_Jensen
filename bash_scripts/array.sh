#!/bin/bash 
MYARRAY=("You cannot shake hands with a clenched fist." "Whoever is happy will make you happy too." "Let us be grateful to people who make us happy." "Very little is needed to make a happy life." "Be happy for this moment. This moment is your life.")

echo ${MYARRAY[0]//happy/sloppy}
echo ${MYARRAY[1]//happy/sloppy}
echo ${MYARRAY[2]//happy/sloppy}
echo ${MYARRAY[3]//happy/sloppy}
echo ${MYARRAY[4]//happy/sloppy}
