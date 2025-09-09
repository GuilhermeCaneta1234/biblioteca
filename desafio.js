// Cena, câmera e renderizador
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({antialias:true});
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Estrada
const roadGeometry = new THREE.PlaneGeometry(10, 2000);
const roadMaterial = new THREE.MeshBasicMaterial({color:0x333333});
const road = new THREE.Mesh(roadGeometry, roadMaterial);
road.rotation.x = -Math.PI/2;
road.position.z = -1000;
scene.add(road);

// Carro do jogador
const carGeometry = new THREE.BoxGeometry(1,1.5,2);
const carMaterial = new THREE.MeshBasicMaterial({color:0xff0000});
const car = new THREE.Mesh(carGeometry, carMaterial);
car.position.y = 0.75;
car.position.z = 0;
scene.add(car);

// Obstáculos
let obstacles = [];
const obstacleGeometry = new THREE.BoxGeometry(1,1.5,2);
const obstacleMaterial = new THREE.MeshBasicMaterial({color:0x0000ff});

let score = 0;
let level = 1;
let speed = 0.5;

// HUD
const scoreEl = document.getElementById("score");
const levelEl = document.getElementById("level");

// Câmera
camera.position.y = 5;
camera.position.z = 10;
camera.lookAt(car.position);

// Movimento
let moveLeft=false;
let moveRight=false;
document.addEventListener("keydown", e => {
    if(e.key==="ArrowLeft") moveLeft=true;
    if(e.key==="ArrowRight") moveRight=true;
});
document.addEventListener("keyup", e => {
    if(e.key==="ArrowLeft") moveLeft=false;
    if(e.key==="ArrowRight") moveRight=false;
});

// Função principal
function animate() {
    requestAnimationFrame(animate);

    // Movimento do carro
    if(moveLeft && car.position.x>-4) car.position.x -= 0.2;
    if(moveRight && car.position.x<4) car.position.x += 0.2;

    // Criar obstáculos
    if(Math.random()<0.02){
        let obs = new THREE.Mesh(obstacleGeometry, obstacleMaterial);
        obs.position.x = Math.floor(Math.random()*9 -4);
        obs.position.y = 0.75;
        obs.position.z = -100;
        obstacles.push(obs);
        scene.add(obs);
    }

    // Mover obstáculos
    obstacles.forEach((obs, index) => {
        obs.position.z += speed;
        // Colisão simples
        if(Math.abs(obs.position.z)<1 && Math.abs(obs.position.x - car.position.x)<1){
            alert("GAME OVER! Pontos: "+score);
            window.location.reload();
        }
        // Obstáculos que passaram
        if(obs.position.z > 10){
            scene.remove(obs);
            obstacles.splice(index,1);
            score++;
            scoreEl.textContent = score;
            if(score%10===0){
                level++;
                levelEl.textContent = level;
                speed +=0.2;
            }
        }
    });

    renderer.render(scene,camera);
}

animate();
