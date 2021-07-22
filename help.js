const message = document.getElementById('message');
const achievement = document.getElementById('achievement');

// Pushing messages
const messages = [
  `Hey...`,
  `Heard that you're feeling down lately,`,
  `Wanna feel better?`,
  `Sometimes when you feel discouraged,`,
  `And wondering if you're actually ACHIEVED something in your life`,
  `Just take a look at what you've made,`,
  `Wish you all the best <3`
]

const addMessage = (msg) => {
  const node = document.createElement('p');
  node.innerText = msg;
  node.classList.add('msg');
  message.appendChild(node);
}

const addMessages = (ind) => {
  if (ind === messages.length) {
    shuffle(achievements);
    console.log(achievements);
    addAchievements(0);
    return;
  }
  addMessage(messages[ind]);
  setTimeout(() => addMessages(ind + 1), 1000);
}

const addAchievement = (acv) => {
  const node = document.createElement('img');
  node.src = acv
  node.classList.add('acv');
  achievement.appendChild(node);
}

const addAchievements = (ind) => {
  if (ind === achievements.length) {
    return;
  }
  addAchievement(achievements[ind]);
  setTimeout(() => addAchievements(ind + 1), 1000);
}

const shuffle = (arr) => {
  n = parseInt(Math.random() * 1000);
  while (n--) {
    a = parseInt(Math.random() * (arr.length - 1));
    b = parseInt(Math.random() * (arr.length - a) + a);
    let tmp = arr[a];
    arr[a] = arr[b];
    arr[b] = tmp;
  }
}

addMessages(0);