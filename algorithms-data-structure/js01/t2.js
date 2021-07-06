function solution(s) {
  const stack = [];

  for (const l of s) {
    if (l !== ')') {
      stack.push(l);
      continue;
    }

    let flag = true;
    let temp = '';

    while (flag) {
      const pl = stack.pop();
      if (pl === '(') flag = false;
      else temp = pl + temp;
    }

    flag = true;
    let num = '';

    while (flag) {
      const n = stack.pop();
      if (/[0-9]/.test(n)) {
        num = n + num;
      } else {
        stack.push(n);
        flag = false;
      }
    }

    stack.push(temp.repeat(+num));
  }
  return stack.join('');
}

console.log(solution('14(a)'));
