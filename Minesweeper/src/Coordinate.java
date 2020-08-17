public class Coordinate {
    private int x;
    private int y;

    public Coordinate(int y, int x){
        this.y = y;
        this.x = x;
    }

    public int getX(){
        return x;
    }

    public int getY() {
        return y;
    }

    public boolean equals(Coordinate other){
        return x == other.getX() && y == other.getY();
    }

    public boolean equals(int y, int x){
        return x == this.x && y == this.y;
    }
}
