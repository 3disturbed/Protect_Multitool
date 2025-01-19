import Sprite from './sprite.js';
import { FROG_CONFIG } from './constants.js';

export const frog = new Sprite({
    ...FROG_CONFIG,
    x: 50,
    y: window.innerHeight / 2
});