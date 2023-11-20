public class primitiveCasting {
    public static void main(String[] args) {
        // Primitive Casting from int to byte
        int intVal = 127;
        byte byteVal = (byte) intVal;
        
        System.out.println("int to byte: " + byteVal);

        // Primitive Casting from byte to int
        int backToInt = byteVal;
        
        System.out.println("byte to int: " + backToInt);
    }
}
