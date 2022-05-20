public class AVector {
    private int size;
    private int capacity;
    private int[] data;

    private static final int MIN_CAPACITY = 16;
    private static final int GROWTH_FACTOR = 2;
    private static final int SHRINK_FACTOR = 4;

    private static int calculateCapacity(int capacity) {
        final int MIN_POSSIBLE_CAPACITY = 1;
        if (capacity < MIN_POSSIBLE_CAPACITY) {
            throw new ArithmeticException("Capacity can not be less than" + MIN_POSSIBLE_CAPACITY);
        }
        
        int realCapacity = MIN_CAPACITY;

        while (capacity > realCapacity / GROWTH_FACTOR) {
            realCapacity *= GROWTH_FACTOR;
        }
        
        return realCapacity;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return capacity;
    }

    public AVector() {
        size = 0;
        capacity = MIN_CAPACITY;
        data = new int[MIN_CAPACITY];
    }
    
    public AVector(int capacity) {
        int realCapacity = calculateCapacity(capacity);

        size = 0;
        this.capacity = capacity;
        data = new int[realCapacity];
    }
    
    private void upsize() {
        int oldCapacity = capacity;
        int newCapacity = calculateCapacity(oldCapacity);
        int[] newData = new int[newCapacity];
        System.arraycopy(data, 0, newData, 0, size);

        data = newData;
        capacity = newCapacity;
    }
    
    private void downsize() {
        int oldCapacity = capacity;
        int newCapacity = oldCapacity / GROWTH_FACTOR;

        if (newCapacity < MIN_CAPACITY) {
            newCapacity = MIN_CAPACITY;
        }
        
        if (newCapacity != oldCapacity) {
            int[] newData = new int[newCapacity];
            System.arraycopy(data, 0, newData, 0, size);

            data = newData;
            capacity = newCapacity;
        }
    }
    
    private void resizeForSize(int candidateSize) {
        if (size < candidateSize) {
            if (size == capacity) {
                upsize();
            }
        } else if (size > candidateSize) {
            if (size < capacity / SHRINK_FACTOR) {
                downsize();
            }
        }
    }
    
    public boolean isEmpty() {
        return size == 0;
    }
    
    private boolean isValidIndex(int index) {
        return index < 0 || index >= size;
    }
    
    public int at(int index) {
        if (!isValidIndex(index)) {
            throw new IndexOutOfBoundsException("Index " + index + " is not valid.");
        }
        return data[index];
    }

    public void at(int index, int value) {
        if (!isValidIndex(index)) {
            throw new IndexOutOfBoundsException("Index " + index + " is not valid.");
        }
        data[index] = value;
    }
    
    public int find(int item) {
        int index = -1;
        for (int i = 0; i < size; i++) {
            if (data[i] == item) {
                index = i;
                break;
            }
        }
        return index;
    }
    
    public void push(int value) {
        resizeForSize(size + 1);
        data[size] = value;
        size++;
    }
    
    public int pop() {
        if (isEmpty()) {
            throw new IndexOutOfBoundsException("Empty error.");
        }
        int poppedValue = data[size - 1];
        resizeForSize(size - 1);
        size--;
        
        return poppedValue;
    }
    
    @Override
    public String toString() {
        StringBuilder dataStr = new StringBuilder();
        dataStr.append("[");
        for (int i = 0; i < size; ++i) {
            dataStr.append(data[i]);
            if (i != size - 1) {
                dataStr.append(", ");
            }
        }
        dataStr.append("]");
        return "AVector [capacity=" + capacity + ", data=" + dataStr.toString() + ", size=" + size + "]";
    }

    public static void main(String[] args) {
        AVector testArray = new AVector();
        System.out.println(testArray);
        
        int TEST_ELEMS = 20;
        for (int i = 0; i < TEST_ELEMS; ++i) {
            testArray.push(i);
            System.out.println(testArray);
        }
        
        for (int i = TEST_ELEMS; i > 3; --i) {
            testArray.pop();
            System.out.println(testArray);
        }
    }
}