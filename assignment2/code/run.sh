export LD_LIBRARY_PATH=/usr/lib/lp_solve

javac -cp ".:lib/lpsolve55j.jar" *.java && \
java -cp ".:lib/lpsolve55j.jar" BnB
