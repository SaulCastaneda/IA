// Data Set
let DataSet='https://teachablemachine.withgoogle.com/models/tl-xiUuLF/';

let Classficador;
let video;
let flipped; 
let label="";
let texto="";
function preload()
{
    classifier = ml5.imageClassifier(DataSet+ 'model.json');
}
function setup()
{
    createCanvas(480,460);
    video= createCapture(VIDEO);
    video.size(320, 240);
    video.hide();

    flipped= ml5.flipImage(video);
    classifyVideo();

}

function draw() {
    background(0);
    // Draw the video
    image(flipped, 0, 0);
  
    if (label === "Andrew Garfield") {
      texto = " \n 🕷🕸⚡ \n Andrew "
    
    } else if (label === "Tom Holland") {
      texto = "\n 🕷🕸⚡ \n Tom "
    } else if (label === "Tobey Maguire") {
      texto = "\n 🕷🕸⚡ \n Tobey"
    }

    // Draw the label
    fill(255);
    textSize(32);
    textAlign(CENTER);
    text(texto, width / 2, height/2);
  }
  
  // Get a prediction for the current video frame
  function classifyVideo() {
    flipped = ml5.flipImage(video)
    classifier.classify(flipped, gotResult);
    flipped.remove();
  
  }
  
  // When we get a result
  function gotResult(error, results) {
    // If there is an error
    if (error) {
      console.error(error);
      return;
    }
    // The results are in an array ordered by confidence.
    // console.log(results[0]);
    label = results[0].label;
    // Classifiy again!
    classifyVideo();
  }