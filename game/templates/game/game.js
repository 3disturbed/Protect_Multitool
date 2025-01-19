// Game loop goes here
import Sprite from './sprite.js';
import { frog } from './frog.js';
import {
    SCROLL_SPEED,
    SURFACE_SCROLL_SPEED,
    WALL_SPACE,
    WALL_SPEED,
    WALL_SPAWN_INTERVAL,
    FLOOR_HEIGHT,
    SURFACE_HEIGHT,
    FRAME_WIDTH,
    KICK_COOLDOWN,
    FLOOR_SPRITE_CONFIG,
    // ... import other constants
} from './constants.js';

let gameStarted = false;
let canKick = true;
let kickCooldown = 0;
let score = 0;
let highScore = 0;
let pipes = [];
let surfaceOffset = 0;
let floorOffset = 0;
let decorations = [];
let walls = [];
let frameCount = 0;

const floorSprite = new Sprite({ ...FLOOR_SPRITE_CONFIG, x: 0, y: 0 });
const surfaceSprite = new Sprite({ imageSrc: './images/surface.png', frameWidth: 32, frameHeight: 32, frames: 1, frameDelay: 100, scaleFactor: 3, opacity: 1, rotation: 0, yFrame: 0, x: 0, y: 0, width: 32, height : 32, velocity: 0, boyancy: 0, jump: 0, alive: true, GullDistance: 0 });
const wallSprite = new Sprite({ mageSrc: './images/wall.png', frameWidth: 16, frameHeight: 16, frames: 1, frameDelay: 100, scaleFactor: 3, opacity: 1,  rotation: 0, yFrame: 0, x: 0, y: 0, width: 16, height: 16, velocity: 0, boyancy: 0, jump: 0, alive: true, GullDistance: 0 });
const canvas = document.getElementById('gameCanvas');
const context = canvas.getContext('2d');


// Handle fullscreen functionality
const playButton = document.getElementById('playButton');
playButton.addEventListener('click', () => {
    if (canvas.requestFullscreen) {
        canvas.requestFullscreen();
    } else if (canvas.mozRequestFullScreen) { // Firefox
        canvas.mozRequestFullScreen();
    } else if (canvas.webkitRequestFullscreen) { // Chrome, Safari and Opera
        canvas.webkitRequestFullscreen();
    } else if (canvas.msRequestFullscreen) { // IE/Edge
        canvas.msRequestFullscreen();
    } 

    playButton.style.display = 'none';
});


// Handle resizing
function resizeCanvas() {
    const maxWidth = window.innerWidth;
    const maxHeight = window.innerHeight;
    const ratio = 720 / 1280;

    let newWidth = maxWidth;
    let newHeight = maxWidth / ratio;

    if (newHeight > maxHeight) {
        newHeight = maxHeight;
        newWidth = maxHeight * ratio;
    }

    canvas.style.width = newWidth + 'px';
    canvas.style.height = newHeight + 'px';
}
window.addEventListener('resize', resizeCanvas);
window.addEventListener('load', resizeCanvas);



// Block in the background
function drawBackground(context) {
    context.fillStyle = 'skyblue';
    context.fillRect(0, 0, canvas.width, canvas.height);
    context.fillStyle = '#5566dd';
    context.fillRect(0, 160, canvas.width, canvas.height); // Water surface
    context.fillStyle = 'brown';
    context.fillRect(0, 1150, canvas.width, canvas.height); // Floor
}   

function drawUI(context) {
    context.fillStyle = 'white';
    context.font = '24px Arial';
    context.fillText('Kicky Frog', 10, 30);
    context.fillText(`Score: ${score}`, 10, 1250);
    context.fillText(`High Score: ${highScore}`, 500, 1250);

}

// Modify drawFloor function
function drawFloor(context) {
    floorOffset = (floorOffset - SCROLL_SPEED) % 32;
    surfaceOffset = (surfaceOffset - SURFACE_SCROLL_SPEED) % 32;

    // Draw floor tiles with parallax
    for (let i = -32 + floorOffset; i < canvas.width + 32; i += 32) {
        floorSprite.setPosition(i, 1150);
        floorSprite.draw(context);
    }
    
    // Draw surface tiles with faster parallax
    for (let i = -32 + surfaceOffset; i < canvas.width + 32; i += 32) {
        surfaceSprite.setPosition(i, 155);
        surfaceSprite.draw(context);
    }
}
// Main game loop
function gameLoop(timestamp) {
    drawBackground(context);
    drawFloor(context);

    drawUI(context);
    requestAnimationFrame(gameLoop);
}

// game input
canvas.addEventListener('touchstart', (e) => {
    e.preventDefault();
    handleJump();
});

// Start game loop
gameLoop();