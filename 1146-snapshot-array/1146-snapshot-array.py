class SnapshotArray:

    def __init__(self, length: int):
        self.snapshotarr = [{} for i in range(length)]
        self.snap_count = 0
        

    def set(self, index: int, val: int) -> None:
        self.snapshotarr[index][self.snap_count] = val

    def snap(self) -> int:
        self.snap_count += 1
        return self.snap_count - 1

    def get(self, index: int, snap_id: int) -> int:
        while snap_id not in self.snapshotarr[index] and snap_id >= 0:
            snap_id -= 1
        if snap_id in self.snapshotarr[index]:
            return self.snapshotarr[index][snap_id]
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)