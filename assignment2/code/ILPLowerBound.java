import lpsolve.*;
import java.io.*;

class ILPLowerBound {
    public static double lowerbound(TCPProblem p, BnBNode n) {
        try {
            int numVertices = p.n;
            int numEdges = numVertices * (numVertices-1);
            int numVars = numVertices + numEdges;

            File program = File.createTempFile("ilp", ".lp");
            BufferedWriter pw = new BufferedWriter( new FileWriter( program ) );

            // File format: http://lpsolve.sourceforge.net/5.5/lp-format.htm

            pw.write("min: " + objective(p) + ";\n");
            pw.write("bin " + binvars(p) + ";\n");

            pw.flush();
            LpSolve solver = LpSolve.readLp(program.getPath(), LpSolve.NORMAL, null);
            // Do stuff with linear program.
            solver.deleteLp();
            program.delete();
        } catch (Exception e) {
            e.printStackTrace();
        }

        return 0;
    }

    private static String objective(TCPProblem p) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < p.n; i++) {
            for (int j = 0; j < p.n; j++) {
                if (i==j) continue;

                sb.append("+ ").append(p.vertices[i].distance(p.vertices[j]))
                  .append(" e_").append(i).append("_").append(j).append(" ");
            }
        }

        return sb.toString();
    }

    private static String binvars(TCPProblem p) {
        boolean begin = true;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < p.n; i++) {
            for (int j = 0; j < p.n; j++) {
                if (i==j) continue;
                if (begin) {
                    begin = false;
                } else {
                    sb.append(", ");
                }

                sb.append(" e_").append(i).append("_").append(j).append(" ");
            }
        }

        return sb.toString();
    }
}
