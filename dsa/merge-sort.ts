// conquor (merge) function
function merge(left: number[], right: number[]) {
    const sorted: number[] = []
    while (left.length && right.length) {
        if (left[0] <= right[0]) {
            sorted.push(left.shift() as number)
        } else {
            sorted.push(right.shift() as number)
        }
    }
    // it's important to maintain the order
    return [...sorted, ...left, ...right]
}

// divide & conquor (merge) - mergeSort function
function mergeSort(arr: number[]): number[] {
    if (arr.length === 1) return arr // base case

    const mid = Math.floor(arr.length / 2) // floor & slice: excluding the mid element
    const left = arr.slice(0, mid) // 0th to (mid-1)th elements
    const right = arr.slice(mid) // omit 2nd args, it'll take upto the last element

    return merge(mergeSort(left), mergeSort(right))
}

const case1 = [5, 4, 6, 3, 9, 8, 2]
// const ansC1 = [2, 3, 4, 5, 6, 8, 9]
console.log(mergeSort(case1))