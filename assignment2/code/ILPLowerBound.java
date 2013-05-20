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
            pw.write(noBranchConstraints(p));
            pw.write(ingoingEqualsOutgoingConstraints(p));
            pw.write(vertexDegreeConstraints(p));
            pw.write(noBidirectionalEdgesConstraints(p));
            pw.write(connectedGraphConstraints(p));
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

        for (int i = 0; i < p.n; i++) {
            sb.append(", w_").append(i);
        }

        return sb.toString();
    }

    private static String noBranchConstraints(TCPProblem p) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < p.n; i++) {
            for (int j = 0; j < p.n; j++) {
                if (i==j) continue;
                sb.append(" + e_").append(i).append("_").append(j)
                  .append(" + e_").append(j).append("_").append(i);
            }
            sb.append(" <= 2;\n");
        }

        return sb.toString();
    }

    private static String ingoingEqualsOutgoingConstraints(TCPProblem p) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < p.n; i++) {
            for (int j = 0; j < p.n; j++) {
                if (i==j) continue;
                sb.append(" + e_").append(i).append("_").append(j)
                  .append(" - e_").append(j).append("_").append(i);
            }
            sb.append(" = 0;\n");
        }

        return sb.toString();
    }

    private static String vertexDegreeConstraints(TCPProblem p) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < p.n; i++) {
            for (int j = 0; j < p.n; j++) {
                if (i==j) continue;
                sb.append(" + e_").append(j).append("_").append(i);
            }
            sb.append("- w_").append(i);

            sb.append(" = 0;\n");
        }

        return sb.toString();
    }

    private static String noBidirectionalEdgesConstraints(TCPProblem p) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < p.n; i++) {
            for (int j = 0; j < i; j++) {
                if (i==j) continue;
                sb.append("e_").append(i).append("_").append(j)
                  .append(" + e_").append(j).append("_").append(i)
                  .append(" <= 1;\n");
            }
        }

        return sb.toString();
    }

    private static String connectedGraphConstraints(TCPProblem p) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < p.n; i++) {
            for (int j = 0; j < p.n; j++) {
                if (i==j) continue;
                sb.append(" + w_").append(j);
            }
            sb.append(" >= 1;\n");
        }

        return sb.toString();
    }
}
