

// let btnStart=document.getElementsByClassName('btnStart')
// btnStart.addEventListener('click', function(){
  // console.log("testing")
  
  const gameContainer = document.getElementById("game");
let clickCount=0;

const COLORS = [
  "red",
  "blue",
  "green",
  "orange",
  "purple",
  "red",
  "blue",
  "green",
  "orange",
  "purple"
]

// here is a helper function to shuffle an array
// it returns the same array with values shuffled
// it is based on an algorithm called Fisher Yates if you want ot research more
function shuffle(array) {
  let counter = array.length;
// 
  // While there are elements in the array
  while (counter > 0) {
    // Pick a random index
    let index = Math.floor(Math.random() * counter);

    // Decrease counter by 1
    counter--;

    // And swap the last element with it
    let temp = array[counter];
    array[counter] = array[index];
    array[index] = temp;
  }
// 
  return array;
}
// 
let shuffledColors = shuffle(COLORS);

// this function loops over the array of colors
// it creates a new div and gives it a class with the value of the color
// it also adds an event listener for a click for each card
function createDivsForColors(colorArray) {
  for (let color of colorArray) {
    // create a new div
    const newDiv = document.createElement("div");

    // give it a class attribute for the value we are looping over
    newDiv.classList.add(color);
    newDiv.classList.add('back');
    //could do the following to the classes on teh div as follows:
    //newDiv.classList.remove('back');
    //newDiv.classList.replace('already exists', 'will be new class')
    //newDiv.classList.replace('back', ')

    // call a function handleCardClick when a div is clicked on
    newDiv.addEventListener("click", handleCardClick);

    // append the div to the element with an id of game
    gameContainer.append(newDiv);
  }

}

// 
// TODO: Implement this function!
let card1="";
let card1Value="";
let card2="";
let card2Value="";


  function handleCardClick(event) {
  // if(topDiv=document.querySelector('div')
    // console.log(event.target)
  // }else {
    // console.log("help")
  // }
  // you can use event.target to see which element was clicked
  clickCount+=1;


  setTimeout(function (){


    if(clickCount===1){
      card1=event.target;
      card1Value=card1.classList.value;
      card1.classList.remove('back');
    }
    if(clickCount===2){
        card2=event.target
        card2Value=card2.classList.value;
        card2.classList.remove('back');
        // console.log(clickCount);
        // console.log(card1);
        // console.log(card2);
        if(card1Value==card2Value){
          // card1.remove();
          // card2.remove();
        }else{
          setTimeout(function (){
            console.log("start timer of 5 secs")
            card1.classList.add('back');
            card2.classList.add('back');
          }, 1000)
        }
        card1.value="";
        card1Value.value="";
        card2.value="";
        card2Value.value="";
        clickCount=0;
        console.log("hi I'm Elfo!!")
      }
      }, 1000)
      console.log("Bye, I'm Elfo")
    }
createDivsForColors(shuffledColors);
  // })