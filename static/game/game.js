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
const wallSprite = new Sprite({ 
    imageSrc: './images/wall.png',  // Fixed 'mageSrc' to 'imageSrc'
    frameWidth: 16, 
    frameHeight: 16, 
    frames: 1, 
    frameDelay: 100, 
    scaleFactor: 3, 
    opacity: 1,  
    rotation: 0, 
    yFrame: 0, 
    x: 0, 
    y: 0, 
    width: 8, 
    height: 8, 
    velocity: 0, 
    boyancy: 0, 
    jump: 0, 
    alive: true, 
    GullDistance: 0 
});
const plantSprite = new Sprite({ 
    imageSrc: './images/plant.png', 
    frameWidth: 64, 
    frameHeight: 64, 
    frames: 2,  // Changed from 1 to 2 frames
    frameDelay: 1500, // Added longer delay for plant animation
    scaleFactor: 1.9, 
    opacity: 1, 
    rotation: 0, 
    yFrame: 0, 
    x: 0, 
    y: 0, 
    width: 64, 
    height: 64, 
    velocity: 0, 
    boyancy: 0, 
    jump: 0, 
    alive: true, 
    GullDistance: 0 
});
const rockSprite = new Sprite({ imageSrc: './images/rock.png', frameWidth: 64, frameHeight: 64, frames: 1, frameDelay: 100, scaleFactor: 2, opacity: 1, rotation: 0, yFrame: 0, x: 0, y: 0, width: 64, height: 64, velocity: 0, boyancy: 0, jump: 0, alive: true, GullDistance: 0 });

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


// Clutter the game with some decorations

function spawnDecoration() {
    if (Math.random() < 0.01) {
        const isPlant = Math.random() < 0.5;
        const randomScale = isPlant ? 
            1.2 + Math.random() * 8.3 :  // Plant scale between 1.2 and 3.5
            1.4 + Math.random() * 5.1;   // Rock scale between 1.4 and 3.5
        
        // Calculate y position based on scale to ensure grounding
        const spriteHeight = (isPlant ? 64 : 64) * randomScale;
        const yPos = 1320 - spriteHeight; // Floor is at 1150
        
        decorations.push({
            sprite: isPlant ? plantSprite : rockSprite,
            x: canvas.width,
            y: yPos,
            passed: false,
            scaleFactor: randomScale,
            parallaxFactor: 0.5 + (1 / randomScale) // Bigger objects move slower
        });
    }
}

function prewarmDecorations() {
    for (let x = 0; x < canvas.width; x += 200) {
        if (Math.random() < 0.5) {
            const isPlant = Math.random() < 0.5;
            const randomScale = isPlant ? 
                1.2 + Math.random() * 8.3 :
                1.4 + Math.random() * 5.1;
            
            const spriteHeight = (isPlant ? 64 : 64) * randomScale;
            const yPos = 1300 - spriteHeight;
            
            decorations.push({
                sprite: isPlant ? plantSprite : rockSprite,
                x: x,
                y: yPos,
                passed: false,
                scaleFactor: randomScale,
                parallaxFactor: 0.5 + (1 / randomScale)
            });
        }
    }
}

function updateDecorations() {
    // Remove decorations when they're one full screen width off the left edge
    decorations = decorations.filter(dec => dec.x > -canvas.width);
    decorations.forEach(dec => {
        dec.x -= SCROLL_SPEED * dec.parallaxFactor;
    });
}

function drawDecorations(context) {
    // First pass: Draw plants (foreground)
    decorations.forEach(dec => {
        if (dec.sprite === plantSprite) {
            dec.sprite.setPosition(dec.x, dec.y);
            dec.sprite.scaleFactor = dec.scaleFactor;
            dec.sprite.draw(context);
        }
    });



    // Second pass: Draw rocks (background)
    decorations.forEach(dec => {
        if (dec.sprite === rockSprite) {
            dec.sprite.setPosition(dec.x, dec.y);
            dec.sprite.scaleFactor = dec.scaleFactor;
            dec.sprite.draw(context);
        }
    });
    
}   


// Block in the background
function drawBackground(context) {
    context.fillStyle = 'skyblue';
    context.fillRect(0, 0, canvas.width, canvas.height);
    context.fillStyle = '#5566dd';
    context.fillRect(0, 160, canvas.width, canvas.height); // Water surface
    context.fillStyle = 'brown';
    context.fillRect(0, 1150, canvas.width, canvas.height); // Floor
}   

function drawUIBar(context) {
    // Top UI bar
    // Draw bar shadow
    context.fillStyle = 'rgba(0, 0, 0, 0.3)';
    context.fillRect(0, 5, canvas.width, 45);
    
    // Draw main bar
    context.fillStyle = 'rgba(0, 0, 0, 0.6)';
    context.fillRect(0, 0, canvas.width, 45);
    
    // Draw top highlight
    context.fillStyle = 'rgba(255, 255, 255, 0.1)';
    context.fillRect(0, 0, canvas.width, 2);
    
    // Draw bottom shadow
    context.fillStyle = 'rgba(0, 0, 0, 0.3)';
    context.fillRect(0, 43, canvas.width, 2);
    // Bottom UI bar
    // Draw bar shadow
    context.fillStyle = 'rgba(0, 0, 0, 0.3)';
    context.fillRect(0, 1205, canvas.width, 45);

    // Draw main bar
    context.fillStyle = 'rgba(0, 0, 0, 0.6)';
    context.fillRect(0, 1200, canvas.width, 45);

    // Draw top highlight
    context.fillStyle = 'rgba(255, 255, 255, 0.1)';
    context.fillRect(0, 1200, canvas.width, 2);

}

function drawUI(context) {
    drawUIBar(context);
    
    // Add text shadow
    context.fillStyle = 'rgba(0, 0, 0, 0.5)';
    context.fillText('Kicky Frog', 12, 32);
    context.fillText(`Score: ${score}`, 32, 1232);
    context.fillText(`High Score: ${highScore}`, 502, 1232);
    
    // Draw main text
    context.fillStyle = 'white';
    context.font = '24px Arial';
    context.fillText('Kicky Frog', 10, 30);
    context.fillText(`Score: ${score}`, 30, 1230);
    context.fillText(`High Score: ${highScore}`, 500, 1230);
}

function drawFrame(context) {
    const frameWidth = 20;
    // Create gradients for each side
    const topGrad = context.createLinearGradient(0, 0, 0, frameWidth);
    const bottomGrad = context.createLinearGradient(0,600 ,  500 , 0);
    const leftGrad = context.createLinearGradient(0, 0, frameWidth, 0);
    const rightGrad = context.createLinearGradient( 0,canvas.width - frameWidth, canvas.width, 0);
    
    // Set gradient colors
    const gradients = [topGrad, bottomGrad, leftGrad, rightGrad];
    gradients.forEach(grad => {
        grad.addColorStop(0, 'rgba(0, 0, 0, 0.5)');
        grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
    });
    
    // Draw frame sides
    context.fillStyle = topGrad;
    context.fillRect(0, 0, canvas.width, frameWidth);
    context.fillStyle = bottomGrad;
    context.fillRect(0, canvas.height - frameWidth, canvas.width, frameWidth);
    context.fillStyle = leftGrad;
    context.fillRect(0, 0, frameWidth, canvas.height);
    context.fillStyle = rightGrad;
    context.fillRect(canvas.width - frameWidth, 0, frameWidth, canvas.height);
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
prewarmDecorations();
function gameLoop(timestamp) {
    const deltaTime = 1/60;
    // Always update frog animation
    frog.update(deltaTime);
    
    // Update position based on kickCooldown
    if (kickCooldown > 0) {
        frog.y = frog.y - frog.velocity;
    } else {
        frog.y = frog.velocity < 1 && frog.y > 160
            ? frog.y >= 1150
                ? 1149
                : frog.y - frog.boyancy
            : frog.y;
    }
          
    drawBackground(context);
    drawFloor(context);
    spawnDecoration();
    updateDecorations();
    drawDecorations(context);
    updateWalls();
    drawWalls(context);
    // Draw frog after updating position
    frog.y = kickCooldown > 0 
        ? frog.y - frog.velocity 
        : frog.velocity < 1 && frog.y > 160 // Adjusted for new water surface
            ? frog.y >= 1150 // Adjusted for new floor height
                ? 1149 
                : frog.y - frog.boyancy 
            : frog.y;

    kickCooldown = kickCooldown > 0 ? kickCooldown - 1 : 0;
    score++;
    frog.setPosition(frog.x, frog.y);
    frog.draw(context); // Draw frog after everything else except UI and frame
    drawFrame(context);
    drawUI(context); // UI is drawn last
    requestAnimationFrame(gameLoop);
}

// game input
canvas.addEventListener('touchstart', (e) => {
    e.preventDefault();
    handleJump();
});
canvas.addEventListener('mousedown', (e) => {
    e.preventDefault();
    handleJump();
});
canvas.addEventListener('keydown', (e) => {
    if (e.key === ' ') {
        e.preventDefault();
        handleJump();
    }
});
function handleJump() {
    if (frog.y < FLOOR_HEIGHT && kickCooldown <= 0) { // Adjusted for new floor height
        frog.velocity = frog.jump;
        kickCooldown = KICK_COOLDOWN;
    }
    if (!gameStarted) {
        gameStarted = true;
    }
}

// Wall functions
function spawnWall() {
    const gapPosition = Math.random() * (canvas.height - WALL_SPACE - 100) + 50;
    walls.push({
        x: canvas.width,
        topHeight: gapPosition,
        bottomY: gapPosition + WALL_SPACE,
        passed: false
    });
}

function updateWalls() {
    // Remove off-screen walls
    walls = walls.filter(wall => wall.x > -16);
    
    // Move walls
    walls.forEach(wall => {
        wall.x -= WALL_SPEED;
        
        // Check for collision
        if (checkCollision(wall)) {
            gameOver();
        }
        
        // Update score
        if (!wall.passed && wall.x < frog.x) {
            wall.passed = true;
            score += 10;
        }
    });
    
    // Spawn new walls
    frameCount++;
    if (frameCount >= WALL_SPAWN_INTERVAL) {
        spawnWall();
        frameCount = 0;
    }
}

function drawWalls(context) {
    walls.forEach(wall => {
        // Draw top wall
        for (let y = 0; y < wall.topHeight; y += 16) {
            wallSprite.setPosition(wall.x, y);
            if(y > 160){ // Adjusted for new water surface height
                 wallSprite.draw(context);
            }
           
        }
        
        // Draw bottom wall
        for (let y = wall.bottomY; y < canvas.height - 100; y += 16) {
            wallSprite.setPosition(wall.x, y);
            if(y < 1150) { // Adjusted for new floor height
                wallSprite.draw(context);
            }
        }
    });
}


// Check for collision with walls
function checkCollision(wall) {
    const frogBox = {
        x: frog.x + 5,
        y: frog.y + 5,
        width: frog.width * frog.scaleFactor - 10,
        height: frog.height * frog.scaleFactor - 10
    };
    
    // Check collision with top wall
    if (frogBox.y < wall.topHeight && 
        frogBox.x + frogBox.width > wall.x && 
        frogBox.x < wall.x + 16) {
        return true;
    }
    
    // Check collision with bottom wall
    if (frogBox.y + frogBox.height > wall.bottomY && 
        frogBox.x + frogBox.width > wall.x && 
        frogBox.x < wall.x + 16) {
        return true;
    }
    
    return false;
}

// Game over function handles alarm triggers
function gameOver() {
    if(score < 420) {
        MainAlarm();
    } 
    if(score > 420 && score < 1200) {
        SecondaryAlarm();
    }
    if (score > highScore) {
        highScore = score;
    }
    gameStarted = false;
    walls = [];
    score = 0;
    frog.y = 50;
    frog.velocity = 0;
    playButton.style.display = 'block';
}

function MainAlarm() {
    fetch('/alarm1/')
        .then(response => response.json())
        alert("Alarm 1")
}

function SecondaryAlarm() {
    fetch('/alarm2/')
        .then(response => response.json())
        alert("Alarm 2")
}


// Start game loop
gameLoop();