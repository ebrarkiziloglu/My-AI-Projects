<br /><br />
<div align="center">
<h1 align="center">Machine-Learning-Basic-Project
</h1>
</div>

I completed [Into to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) course on Kaggle, and I created this repo as an exercise.

Here, I used the rental unit information as the data.

## How did I use the data

<ul>
  <li>First, I read the data using pandas.
  <li>Then, I determined the X and y values.
  <li>For X, I chose some of the columns from the data table.
  <li>For y, I chose the 'Price' column.
  <li>Then, I split the given data into training and validation data, 
    using  <a href="https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html">train_test_split</a> 
    method from the <a href="https://scikit-learn.org/">sklearn</a> ML library.
</ul>

## The Data

The data includes information for 13580 rental units. For each house, following records are given:
<ul>
  <li>Suburb's name</li>
  <li>Address</li>
  <li>Rooms</li>
  <li>Type of the unit</li>  
  <li>Price</li>  
  <li>Method of rent</li>  
  <li>Seller's name</li>  
  <li>Date of announcement</li>  
  <li>Distance to the city center</li>
  <li>Postcode</li>
  <li>Number of bedrooms</li>
  <li>Number of bathrooms</li>
  <li>Number of cars that can fit in the garage</li>
  <li>Size of the land</li>
  <li>Area of the building</li>
  <li>Built year</li>
  <li>Council area</li>
  <li>Lattitude</li>
  <li>Longtitude</li>
  <li>Name of the region</li>
  <li>Property count</li>
</ul>

  
  
<div>
<h2>Execution <img src = "https://media2.giphy.com/media/QssGEmpkyEOhBCb7e1/giphy.gif?cid=ecf05e47a0n3gi1bfqntqmob8g9aid1oyj2wr3ds3mg700bl&rid=giphy.gif" width = 28px></h2>
</div>

To execute the script, run the following command:
```sh
python3 basic_melb_model.py
```

