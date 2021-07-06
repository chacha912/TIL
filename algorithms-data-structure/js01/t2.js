function solution(s) {
  const stack = [];

  for (const l of s) {
    if (l !== ')') {
      stack.push(l);
      continue;
    }

    let temp = '';
    while (true) {
      const pl = stack.pop();
      if (pl === '(') break;
      else temp = pl + temp;
    }

    let num = '';
    while (true) {
      const n = stack.pop();
      if (/[0-9]/.test(n)) {
        num = n + num;
      } else {
        stack.push(n);
        break;
      }
    }

    stack.push(temp.repeat(+num));
  }
  return stack.join('');
}

console.log(solution('14(a)'));
