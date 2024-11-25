// merge two sorted arrays

const a1 = [1, 2, 4]
const a2 = [5, 6, 7]

function mergeSorted(a1: number[], a2: number[]) {
    const sorted: number[] = []
    while (a1.length && a2.length) {
        if (a1[0] <= a2[0]) {
            sorted.push(a1.shift() as number)
        } else {
            sorted.push(a2.shift() as number)
        }
    }
    return [...sorted, ...a1, ...a2]
}

console.log(mergeSorted(a1, a2))