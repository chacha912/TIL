function solution(s) {
  let answer = '';
  const arr = [];
  const obj = {};
  for (const l of s) {
    obj[l] = l in obj ? obj[l] + 1 : 1;
  }
  for (const v of Object.entries(obj)) {
    arr.push(v);
  }
  arr.sort((x, y) => y[1] - x[1]);

  for (const [v, i] of arr) {
    for (let j = 0; j < i; j++) {
      answer += v + '';
    }
  }

  return answer;
}

console.log(solution('ABCCAaABBCCAAab')); // AAAAACCCCBBBaab
