// Game loop goes here
import Sprite from './sprite.js';
import { frog } from '../Protect_Multitool/game/templates/game/frog.js';
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

const canvas = document.getElementById('gameCanvas');
const context = canvas.getContext('2d');
const playButton = document.getElementById('playButton');

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