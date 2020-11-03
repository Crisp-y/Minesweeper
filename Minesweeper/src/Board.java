import java.util.*;

public class Board {
    int rows;
    int columns;
    int mines;
    BoardArray board;

    public Board(int rows, int columns, int mines){
        this.rows = rows;
        this.columns = columns;
        this.mines = mines;
        board = new BoardArray();
        for (int i = 0; i < rows;i++) {
            ArrayList<Tile> newRow = new ArrayList<>(columns);
            for (int j = 0; j < columns; j++) {
                newRow.add(new Tile());
            }
            board.add(newRow);
        }
    }

    // Place mines in the board
    public void generateMines(Coordinate start){
        ArrayList<Coordinate> coords = new ArrayList<>();
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                if (!start.equals(i, j)) {
                    coords.add(new Coordinate(i, j));
                }
            }
        }
        Random random = new Random();
        for (int i = 0; i < mines; i++){
            // Remove to avoid choosing the same one
            Coordinate newPos = coords.remove(random.nextInt(coords.size()));
            board.get(newPos).setMine();
            // Change the count of nearby mines
            ArrayList<Coordinate> surroundCoords = newPos.getSurrounds();
            for (Coordinate tile : surroundCoords) {
                board.get(newPos).changeMines(1);
            }
        }

    }

    public int getRows(){ return rows;}
    public int getColumns(){ return columns;}
    public ArrayList<ArrayList<Tile>> getBoard(){ return board;}
    //Add a printing method for testing
    // Consider a unique board class with .get(Coordinate)
}

// Class for specifically the array of tiles, allows easier get() calls
class BoardArray extends ArrayList<ArrayList<Tile>>{
    public Tile get(Coordinate c){
        return this.get(c.getY()).get(c.getX());
    }
}