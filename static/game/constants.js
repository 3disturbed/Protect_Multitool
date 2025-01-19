import { frog } from "./frog";

// Game mechanics
export const SCROLL_SPEED = 1;
export const SURFACE_SCROLL_SPEED = 2;
export const WALL_SPACE = 300;
export const WALL_SPEED = 2;
export const WALL_SPAWN_INTERVAL = 550;
export const FLOOR_HEIGHT = 1150;
export const SURFACE_HEIGHT = 160;
export const FRAME_WIDTH = 20;
export const KICK_COOLDOWN = 10;

// Sprite configurations
export const FROG_CONFIG = {
    imageSrc: frogImg,
    frameWidth: 50,
    frameHeight: 50,
    frames: 2,
    frameDelay: 10,
    scaleFactor: 1.5,
    opacity: 0.8,
    rotation: 45,
    yFrame: 0,
    width: 48,
    height: 48,
    velocity: 0,
    boyancy: 2,
    jump: -8,
    alive: true,
    GullDistance: 500
};

export const FLOOR_SPRITE_CONFIG = {
    imageSrc: floorImg,
    frameWidth: 32,
    frameHeight: 32,
    frames: 1,
    frameDelay: 100,
    scaleFactor: 1,
    opacity: 1,
    rotation: 0,
    yFrame: 0,
    width: 32,
    height: 32
};
