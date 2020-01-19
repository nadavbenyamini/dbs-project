function titleCase(s) {
    const sentence = s.toLowerCase().replace('_',' ').split(" ");
    for(let i = 0; i < sentence.length; i++){
        sentence[i] = sentence[i][0].toUpperCase() + sentence[i].slice(1);
    }
    return sentence.join(' ');
}

function delay(callback, ms) {
  let timer = 0;
  return function() {
    const context = this, args = arguments;
    clearTimeout(timer);
    timer = setTimeout(function () {
      callback.apply(context, args);
    }, ms || 0);
  };
}