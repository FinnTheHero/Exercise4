public class referenceCasting {
    public static void main(String[] args) {
        // Boxing: Converting int to Integer
        Integer intVal = Integer.valueOf(42);

        // Reference casting from Integer to Byte
        Byte byteVal = (byte) intVal.byteValue();

        System.out.println("Integer to Byte: " + byteVal);

        // Unboxing: Converting Integer to int
        int backToInt = intVal.intValue();

        System.out.println("Byte to Integer: " + backToInt);
    }
}
