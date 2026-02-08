const sentences = [
    "Wake up, Neo...",
    "The Matrix has you...",
    "Follow the white rabbit."
];

const textElement = document.getElementById("matrix-text");
const whiteRabbit = document.querySelector("#white-rabbit-png");
const homePageBtn = document.querySelector(".home-page-btn a");

let sentenceIndex = 0;
let charIndex = 0;


function typeSentence() {
    if (charIndex < sentences[sentenceIndex].length) {
        textElement.textContent += sentences[sentenceIndex].charAt(charIndex);

        charIndex++;
        setTimeout(typeSentence, 200); 
    } else {

        if (sentenceIndex < sentences.length - 1) {
            setTimeout(deleteSentence, 1200); 
        } else {

            whiteRabbit.classList.add("show-final");
            homePageBtn.classList.add("show-final");
        }
    }
}

function deleteSentence() {
    if (charIndex > 0) {
        textElement.textContent = sentences[sentenceIndex].substring(0, charIndex - 1);
        charIndex--;
        setTimeout(deleteSentence, 30); 
    } else {
        sentenceIndex++;
        setTimeout(typeSentence, 400);
    }
}

document.addEventListener("DOMContentLoaded", typeSentence());
