const nums = [1, 2, 3, 4];

function productExceptSelf(nums) {
  let temp = 1;

  let answer = [...nums].reverse().map(v => {
    const val = temp;
    temp *= v;
    return val;
  });

  temp = 1;
  answer = [...answer].reverse().map((v, i) => {
    const val = temp;
    temp *= nums[i];
    return v * val;
  });

  return answer;
}

console.log(productExceptSelf(nums));
