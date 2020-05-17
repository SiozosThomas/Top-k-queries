# Top-k-queries

Στόχος του project είναι να παίρνει σαν αρχεία εισόδου στατιστικά με τις
επιδόσεις παικτών που αγωνίστηκαν στο NBA το 2017. Σύμφωνα με τα στατιστικά
που μας ενδιαφέρουν θα βρίσκει τους κορυφαίους k. Η συνάρτηση συνάθροισης θα
είναι το άθροισμα των ομαλοποιημένων επιδόσεων σε καθένα από τα δοθέντα στατιστικά.
Δηλαδή, αν η παράμετρος είναι (2,5), τότε το σκορ του κάθε παίκτη στο στατιστικό 2
(assists) θα είναι ο αριθμός των assists του παίκτη διά το μέγιστο αριθμό assists
που υπάρχει στην πρώτη γραμμή του αρχείου "2018_AST.csv", όμοια και για το στατιστικό
5 (points). Προσθέτοντας αυτά τα 2 σκορ παίρνουμε το συνολικό σκορ του παίκτη σε
αυτά τα δύο στατιστικά. Το πρόγραμμα τυπώνει στην έξοδο τους k κορυφαίους μαζί με
τα συνολικά τους σκορ, καθώς και τον αριθμό των γραμμών που έχουν διαβαστεί από
τα αρχεία (number of accesses).

## Data

Τα δεδομένα προέρχονται από την ιστοσελίδα στατιστικών του NBA.<br/>
[link](https://www.basketball-reference.com/)<br/>
Κατέβηκαν από: https://www.kaggle.com/drgilermo/nba-players-stats και επεξεργάστηκαν.
Τα αρχεία που χρησιμοποιούνται βρίσκονται στον φάκελο "data".


## Running the project

Τα αρχεία εισόδου βρίσκονται στον φάκελο "data".<br/>
* 2017_ALL.csv
* 2017_TRB.csv
* 2017_AST.csv
* 2017_BLK.csv
* 2017_PTS.csv
* 2017_STL.csv

## Output File

Command-line arguments: 1, 2, 5
![Alt Text](/output/result.png)
