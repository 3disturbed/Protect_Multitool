// Sprite class for creating and rendering sprites
export default class Sprite {
    constructor({ imageSrc, frameWidth, frameHeight, frames, frameDelay, scaleFactor, opacity, rotation, yFrame, x, y, width, height, velocity, boyancy, jump, alive, GullDistance }) {
        this.image = new Image();
        this.loaded = false;
        this.image.onload = () => {
            this.loaded = true;        
            console.log("IMG = " + imageSrc);
        };

        this.image.src = imageSrc;
        this.frameWidth = frameWidth;
        this.frameHeight = frameHeight;
        this.frames = frames;
        this.frameDelay = frameDelay;
        this.scaleFactor = scaleFactor;
        this.opacity = opacity;
        this.rotation = rotation;
        this.yFrame = yFrame;
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.velocity = velocity;
        this.boyancy = boyancy;
        this.jump = jump;
        this.alive = alive;
        this.GullDistance = GullDistance;
        this.currentFrame = 0;
        this.frameTimer = 0;
        this.lastUpdate = Date.now(); // Add this line
    }

    update() {
        const now = Date.now();
        if (now - this.lastUpdate >= this.frameDelay) {
            this.currentFrame = (this.currentFrame + 1) % this.frames;
            this.lastUpdate = now;
        }
    }

    draw(context) {
        if (!this.loaded) return;
        
        this.update(); // Add this line to update animation
        
        context.save();
        context.globalAlpha = this.opacity;
        context.translate(this.x + this.width / 2, this.y + this.height / 2);
        context.rotate((this.rotation * Math.PI) / 180);
        context.drawImage(
            this.image,
            this.currentFrame * this.frameWidth,
            this.yFrame * this.frameHeight,
            this.frameWidth,
            this.frameHeight,
            -this.width / 2,
            -this.height / 2,
            this.width * this.scaleFactor,
            this.height * this.scaleFactor
        );
        context.restore();
    }

    setPosition(x, y) {
        this.x = x;
        this.y = y;
    }
}