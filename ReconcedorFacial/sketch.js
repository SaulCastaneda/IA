            // RECONOCEDOR FACIAL DE SPIDERMAN
// Data Set
let DataSet='https://teachablemachine.withgoogle.com/models/Sc-IMSrdW/';
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
    // Imprimir Video
    image(flipped, 0, 0);
    // Validaciones del de data set
  
    if (label === "Andrew Garfield") {
      texto = " \n 🕷🕸⚡ \n Andrew "
    
    } else if (label === "Tom Holland") {
      texto = "\n 🕷🕸⚡ \n Tom "
    } else if (label === "Tobey Maguire") {
      texto = "\n 🕷🕸⚡ \n Tobey"
    }else if(label === "Alfred Molina"){
      texto = "\n 🕷🕸⚡ \n Alfred Molina"
    }
    else if(label === "Willem Defoe"){
      "\n 🕷🕸⚡ \n Willem Defoe"
    }
    // Marcos de Reconocerdor
    fill(255);
    textSize(32);
    textAlign(CENTER);
    text(texto, width / 2, height/2);
  }
  // MEtodo de Clasificar datos del data set
  function classifyVideo() {
    flipped = ml5.flipImage(video)
    classifier.classify(flipped, gotResult);
    flipped.remove();
  }
  // Imprimir resultados
  function gotResult(error, results) {
    // Validacion de Error imprimir el error
    if (error) {
      console.error(error);
      return;
    }
    // Array de resutlatados
    label = results[0].label;
    // funcion de Clasifiacion JS
    classifyVideo();
  }